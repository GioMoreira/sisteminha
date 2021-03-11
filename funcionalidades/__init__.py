def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception:
        print('\033[1;31mErro ao criar arquivo.\033[m')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception:
        print('\033[1;31mErro ao ler arquivo!\033[m')
    else:
        for li in a:
            dado = li.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[1m{dado[0]:<30}{dado[1]:>3} anos\033[m')
    finally:
        a.close()


def cadastrar(arq, n='desconhecido', i=0):
    try:
        a = open(arq, 'at')
    except Exception:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except Exception:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print('Novo registro adicionado.')
            a.close()
