class Grafo:

    #def graph(self, vertices):
    edges = 0

    def __init__(self, vertices):
        #graph(self, vertices)
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def loadData(self, nome_arquivo, vertices):
        v=0
  
        with open(nome_arquivo,'r') as arquivo:
          for linha in arquivo:
            if v==0:
              edges = linha #recebendo o número de vértices da primeira linha
            else:   
              #print(linha)
             
              valores = linha.split()
              #print("********", valores)
            #contar a+= numDeArestas a partir do length de valores
              self.adiciona_aresta(int(valores[0]), int(valores[1]))
            v += 1
            
        self.numEdges(edges)
            
    def adiciona_aresta(self, u, v):
        # pensando em grafo não direcionado sem peso nas arestas
        self.grafo[v-1].append(u)
        self.grafo[u-1].append(v)

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

    #def numVertex():
  
    def numEdges(numCont, edges):
        print('Numero de vertices contados: ', numCont)
        print('Numero de vertices dados: ', edges)
        return edges

file = 'dblp.txt'
g = Grafo(1397510) #ver numero de linhas

g.loadData(file, 1397510)

#g.adiciona_aresta(1,2) #apenas testes, deve chamar cada linha do arquivo e inserir aqui
#g.adiciona_aresta(1,3)
#g.adiciona_aresta(1,4)
#g.adiciona_aresta(2,3)

g.mostra_lista()
g.numEdges(edges)