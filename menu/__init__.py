def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida.\033[m')
            return 0
        else:
            return n


def linha(tam=40):
    print('-' * tam)


def titulo(palavra):
    linha()
    print(palavra.center(40))
    linha()


def opcoes(op):
    for k, v in op.items():
        print(f'\033[33m{k} - \033[m', end='')
        print(f'\033[34m{v}\033[m')
    linha()
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc
