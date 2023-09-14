#===============================================================================
# Exemplo: segmentação de uma imagem em escala de cinza.
#-------------------------------------------------------------------------------
# Autor: Bogdan T. Nassu
# Universidade Tecnológica Federal do Paraná
#-------------------------------------------------------------------------------
# Aluno: Lucian Augusto
# RA: 1175262
#===============================================================================
import sys
import timeit
import numpy as np
import cv2
from component import Component

#===============================================================================
INPUT_IMAGE =  'arroz.bmp'

# TODO: ajuste estes parâmetros!
NEGATIVO = False
THRESHOLD = 0.8
ALTURA_MIN = 5
LARGURA_MIN = 5
N_PIXELS_MIN = 30

#===============================================================================
#------------------------------- Binariation -----------------------------------
def binariza (img, threshold):
    ''' Binarização simples por limiarização.

Parâmetros: img: imagem de entrada. Se tiver mais que 1 canal, binariza cada
              canal independentemente.
            threshold: limiar.
            
Valor de retorno: versão binarizada da img_in.'''

    return np.where(img <= threshold, 0, 1, ).astype(np.float32)

# ---------------------------- Flood Fill Labeling -----------------------------
# Flood Fill Algorithm
def flood_fill(image, y, x, label) -> Component:
    image[y, x, 0] = label
    height, width, _ = image.shape
    component = Component(label, 1, y, x, y, x)

    for y_neighbor, x_neighbor in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
        if (x_neighbor >= 0 and x_neighbor < width and y_neighbor >= 0 and y_neighbor < height and (0.0 < image[y_neighbor, x_neighbor, 0] < 1.1)):
            neighbor = flood_fill(image, y_neighbor, x_neighbor, label)
            component.top = min(component.top, neighbor.top)
            component.left = min(component.left, neighbor.left)
            component.bottom = max(component.bottom, neighbor.bottom)
            component.right = max(component.right, neighbor.right)

    return component

# Labeling Function
def rotula (img, largura_min, altura_min, n_pixels_min):
    '''Rotulagem usando flood fill. Marca os objetos da imagem com os valores
[0.1,0.2,etc].

Parâmetros: img: imagem de entrada E saída.
            largura_min: descarta componentes com largura menor que esta.
            altura_min: descarta componentes com altura menor que esta.
            n_pixels_min: descarta componentes com menos pixels que isso.

Valor de retorno: uma lista, onde cada item é um vetor associativo (dictionary)
com os seguintes campos:

'label': rótulo do componente.
'n_pixels': número de pixels do componente.
'T', 'L', 'B', 'R': coordenadas do retângulo envolvente de um componente conexo,
respectivamente: topo, esquerda, baixo e direita.'''

    height, width, _ = img.shape

    label = 1.1
    components = []

    for y in range(height):
        for x in range(width):
            if (0.0 < img[y, x, 0] < 1.1):
                new_component = flood_fill(img, y, x, label)
                if (new_component.validate(largura_min, altura_min, n_pixels_min)):
                    print(str(new_component.convert_to_tuple()))
                    components.append(new_component.convert_to_tuple())
                    label = label + 0.1
    return components

#===============================================================================
def main ():

    # Abre a imagem em escala de cinza.
    img = cv2.imread (INPUT_IMAGE, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print ('Erro abrindo a imagem.\n')
        sys.exit ()

    # É uma boa prática manter o shape com 3 valores, independente da imagem ser
    # colorida ou não. Também já convertemos para float32.
    img = img.reshape ((img.shape [0], img.shape [1], 1))
    img = img.astype (np.float32) / 255

    # Mantém uma cópia colorida para desenhar a saída.
    img_out = cv2.cvtColor (img, cv2.COLOR_GRAY2BGR)

    # Segmenta a imagem.
    if NEGATIVO:
        img = 1 - img
    img = binariza (img, THRESHOLD)
    cv2.imshow ('01 - binarizada', img)
    cv2.imwrite ('01 - binarizada.png', img*255)

    start_time = timeit.default_timer ()
    componentes = rotula (img, LARGURA_MIN, ALTURA_MIN, N_PIXELS_MIN)
    n_componentes = len (componentes)
    print ('Tempo: %f' % (timeit.default_timer () - start_time))
    print ('%d componentes detectados.' % n_componentes)

    # Mostra os objetos encontrados.
    for c in componentes:
        cv2.rectangle (img_out, (c ['L'], c ['T']), (c ['R'], c ['B']), (0,0,1))

    cv2.imshow ('02 - out', img_out)
    cv2.imwrite ('02 - out.png', img_out*255)
    cv2.waitKey ()
    cv2.destroyAllWindows ()


if __name__ == '__main__':
    main ()

#===============================================================================
