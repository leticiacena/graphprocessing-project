class Grafo:

    def __init__(self): # Função de criar um novo grafo vazio - Graph - Escolhemos o metódo de iniciar a classe para representá-la.
        self.grafo = []

    def Ler_arquivo(self, nome_arquivo): # Função de loadData para carregar um grafo a partir de um arquivo.
        contador = 0
  
        with open(nome_arquivo,'r') as arquivo:
          for linha in arquivo:
            if contador ==0:
              self.grafo = [[] for vertice in range(int(linha))]
              contador +=1
            else:   
              valores = linha.split()
              self.adiciona_aresta(self, int(valores[0]), int(valores[1]))
            
    def adiciona_aresta(self, vertice1, vertice2): # Função auxiliar para adicionar arestas na lista de adjacência.
        self.grafo[vertice2-1].append(vertice1)
        self.grafo[vertice1-1].append(vertice2)

    def mostra_lista(self): # Função que mostra a estrutura de lista de adjacência do grafo.
        for vertice in range(1, self.quantidade_vertice(self)+1):
            print(f'{vertice}:', end='  ')
            for vertice_adjacente in self.grafo[vertice]:
                print(f'{vertice_adjacente}  ->', end='  ')
            print('')
  
    def quantidade_vertice(self): # Função 
        return len(self.grafo)
      
    def quantidade_aresta(self):
      contador = 0
      for vertice in range(1, self.quantidade_vertice(self)+1):
        for vertice_adjacente in self.grafo[vertice-1]:
          if vertice_adjacente > vertice:
            contador+=1
          elif vertice_adjacente == vertice:
            contador+=0.5  
      return int(contador)

    def grau_minimo(self):
        minimo = float('inf')
        for vertice in self.grafo:
            if (len(vertice) < minimo):
                minimo = len(vertice)
        return minimo

    def maxDegree(self):
        max = 0
        maxEdge = 0
        for i in self.grafo:
            if (len(i) > max):
                max = len(i)
                maxEdge = self.grafo.index(i)+1
        return [max, maxEdge]

    def components(self):
        conected_components_quantity = 1
        quantidade_vertice = self.quantidade_vertice(self)

        conected_components_array = self.aux_components(self)

        for index in range(quantidade_vertice):
            if index + 1 not in conected_components_array:
                conected_components_array + self.aux_components(self, index, conected_components_array)
                conected_components_quantity+=1
        
        return conected_components_quantity
                

    def aux_components(self, index=0, markedVertices = []):
        markedVertices.append(index+1)
        pilha = [index+1]

        while pilha:
            vertice = pilha.pop()
            for adjacente in self.grafo[vertice-1]:
                if adjacente not in markedVertices:
                    markedVertices.append(adjacente)
                    pilha.append(adjacente)
            
        return markedVertices
