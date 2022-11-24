class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        # pensando em grafo nãodirecionado sem peso nas arestas
        self.grafo[v-1].append(u)
        self.grafo[u-1].append(v)


    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')
    
    def minDegree(self):
        min = float('inf')
        for i in self.grafo:
            if (len(i) < min):
                min = len(i)
        return min

    def maxDegree(self):
        max = 0
        for i in self.grafo:
            if (len(i) > max):
                max = len(i)
        return max

    def components(self):
        index = 0
        conected_components_quantity = 1

        conected_components_array = self.aux_components(index)

        for i in range(len(self.grafo)):
            if i+1 not in conected_components_array:
                conected_components_array + self.aux_components(i)
                conected_components_quantity+=1
        
        return conected_components_quantity
                

    def aux_components(self, index=0, markedVertices = []):
        markedVertices.append(index+1)

        for adjOfVertice in self.grafo[index]:
            if adjOfVertice not in markedVertices:
                self.aux_components(adjOfVertice-1, markedVertices)
        
        return markedVertices


g = Grafo(7)

g.adiciona_aresta(1,2) #apenas testes, deve chamar cada linha do arquivo e inserir aqui
g.adiciona_aresta(1,3)
g.adiciona_aresta(1,4)
g.adiciona_aresta(2,3)
g.adiciona_aresta(5,6)
g.adiciona_aresta(5,7)
g.adiciona_aresta(6,7)

g.mostra_lista()

print(g.minDegree())
print(g.maxDegree())

print(g.components())