import listaAdjacencias as la

g = la.Grafo

g.Ler_arquivo(g, "dblp.txt")

print(f"Número de pesquisadores: {g.quantidade_vertice(g)}.\n")
print(f"Número de colaborações: {g.quantidade_aresta(g)}.\n")
col_pesq = g.maxDegree(g)
print(f"O id do pesquisador que mais colaborou é ID:{col_pesq[1]} e ele teve {col_pesq[0]} colaborações.\n")
print(f"A menor quantidade de colaboraçoes de um pesquisador foi {g.grau_minimo(g)}.\n")
print(f"A quantidade de subredes de colaboração foram: {g.components(g)} subredes.")
