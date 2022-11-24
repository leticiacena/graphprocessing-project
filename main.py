import listaAdjacencias as la
#t = la.Grafo

file = 'dblp.txt'
g = la.Grafo #ver numero de linhas

g.loadData(file, 1397510, ' ')

#def loadData(nome_arquivo, vertices, separador):
#  a=1
#  
#  with open(nome_arquivo,'r') as arquivo:
#    for linha in arquivo:
#        print(linha)
#        t.adiciona_aresta(linha, a, linha.length)
#        a += 1
      
#file = 'dblp.txt'
#readFile(file)



#readFile('dblp.txt')

#nome_arquivo = sys.argv[1]
#arquivo = open(nome_arquivo)
#linhas = arquivo.readlines()

#for linha in linhas:
#  print(linha)

  #return 1