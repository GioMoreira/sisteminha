from Aula23.desafio115.menu import *
from Aula23.desafio115.funcionalidades import *
from time import sleep


dados = 'cursoemvideo.txt'
if not arquivo_existe(dados):
    criar_arquivo(dados)
central = {1: 'Ver pessoas cadastradas', 2: 'Cadastrar nova pessoa', 3: 'Sair do sistema'}
while True:
    titulo('MENU PRINCIPAL')
    resposta = opcoes(central)
    if resposta == 1:
        titulo('PESSOAS CADASTRADAS')
        ler_arquivo(dados)
        # Ao invés de utilizar módulos como acima, posso fazer diretamente um teste nesta condição:
        # try:
        #    dados = open('cursoemvideo.txt', 'rt')
        # except FileNotFoundError:
        #    dados = open('cursoemvideo.txt, 'wt')
        # print(dados.read())
        # É uma solução mais curta e simples, apesar de não utilizar métodos de checagem e criação separados, utilizados
        # no começo do código.
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(dados, nome, idade)
    elif resposta == 3:
        titulo('SAINDO DO SISTEMA... ATÉ LOGO')
        sleep(1)
        break
    else:
        print('\033[1;31mERRO! Opção Inválida!\033[m')
        sleep(1.5)
