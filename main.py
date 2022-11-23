import listaAdjacencias as la

def readFile(nome_arquivo):
  with open(nome_arquivo,'r') as arquivo:
    for linha in arquivo:
        print(linha)

file = 'dblp.txt'
#readFile(file)

t = la.Grafo

#readFile('dblp.txt')

#nome_arquivo = sys.argv[1]
#arquivo = open(nome_arquivo)
#linhas = arquivo.readlines()

#for linha in linhas:
#  print(linha)

  #return 1