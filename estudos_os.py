import os 
from itertools import count

# o os.system pode ser usado como terminal, entao a maioria dos comandos q pegarem no seu terminal vai pegar por ele 
#os.system('clear')
#os.system('python calen.py')

# o os.path cuida de caminhos 
# o os.path.split() divide o diretorio passado em caminho e nome do arquivo 
#caminho, arquivo = os.path.split(os.path.join(os.getcwd(), 'estudos_os.py'))
#print(caminho, arquivo)

# temos tbm o os.path.splittext() q separa o nome do arquivo da extensao do arquivo 
#nome, extensao = os.path.splitext(arquivo)
#print(nome, extensao)

# o os.path.exists() verifica se a pasta ou o arquivo existe no diretorio especisifcado
#existe = os.path.exists(os.path.join(os.getcwd(), 'tese.py'))
#print(existe)

# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
