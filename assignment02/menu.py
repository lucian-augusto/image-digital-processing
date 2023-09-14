def capture_option() -> int:
    return int(input('''
Por favor, selecione qual algoritmo deve ser utilizado:
(1) - Implementcao Ingenua
(2) - Impementacao Separavel
(3) - Implementacao utilizando Imagem Integral
(0) - Sair

Opcao: '''))

def validate_option(option: int) -> int:
    if 0 <= option <= 3:
        return option
    return -1

def menu() -> int:
    option = -1;
    while(option < 0):
        option = validate_option(capture_option())

    return option
