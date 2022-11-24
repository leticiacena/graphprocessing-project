import listaAdjacencias as la
#t = la.Grafo

file = 'dblp.txt'
g = la.Grafo #ver numero de linhas

g.loadData(file, 1397510)

print(f"Número de pesquisadores: {g.numEdges()}")
print(f"Número de colaborações: {g.numVertex()}")
print("Id do pesquisador que mais colaborou e quantas foram as colaborações:")
col_pesq = g.maxDegree()
print(f"O id do pesquisador que mais colaborou é ID:{col_pesq[1]} e ele teve {col_pesq[0]} colaborações.")
print("Menor colaboração:")
print(f"A menor quantidade de colaboraçoes de um pesquisador foi {g.minDegree()}")
print("Número de subredes de colaboração:")
print(f"A quantidade de subredes de colaboração foram: {g.components()} subredes")
