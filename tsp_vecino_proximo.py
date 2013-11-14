import matplotlib.pyplot as plt
import networkx as nx
import sys



def visitar_nodo(grafo,nodo):
    
     
    tupla = ()
    menor_peso = 11
    pesos = nx.get_edge_attributes(grafo,'weight')
    #x es el vecino
    #y es la tupla de la arista
    
    
    """for y in pesos:
      if len(visitados) < len(grafo.nodes()):
        print("nodo inicio:")
        print(nodo_inicio)
        if nodo in y and (nodo_vecino(y,nodo)) not in visitados and nodo_inicio not in y:
           if pesos[y] < menor_peso:
              menor_peso = pesos[y]
              tupla = y
      elif nodo in y and (nodo_vecino(y,nodo)) not in visitados:
          if pesos[y] < menor_peso:
             menor_peso = pesos[y]
             tupla = y    
    """
    vecinos_visitados = len(visitados)
    for x in grafo.neighbors(nodo):
       for y in pesos:
         if x in y: #el vecino esta en la arista
           if x not in visitados: # el vecino no esta visitado
              if vecinos_visitados < (len(grafo.nodes())-1): # mientas no tenga visitado al origen
                 if nodo_inicio not in y:
                    if pesos[y] < menor_peso: # buscando el menor peso
                       menor_peso = pesos[y]
                       nodo = x
              else:
                nodo = x      
                     
                 
             
           
         
            
    
    
    
          
    
    
    
    #nodo = nodo_vecino(tupla,nodo)
    print("el nodo visitado es")
    print(nodo)
    grafo.node[nodo]['visitado'] = 1
    print("el nodo se marco como visitado")
    print(grafo.node[nodo]['visitado'])
    nada = str(input())
    visitados.append(nodo)
    print("nodos visitados")
    print(visitados)
    if todos_visitados(grafo) == False:
     print("hola")
     visitar_nodo(grafo,nodo)
    else:
       visit = nx.get_node_attributes(grafo,'visitado')
       print(visit)
       return visitados
    
    
         
              
       
 
def todos_visitados(grafo):
     
     lista_visitados = nx.get_node_attributes(grafo,'visitado')
     print("lista de los visitados")
     print(lista_visitados)    
     for x in grafo.nodes():
        if lista_visitados[x] == 0:
         return False
         
     return True 	  
	  
      
       
def nodo_vecino(tupla,nodo):
  if tupla[0] == nodo:
   return tupla[1]
  else:
   return tupla[0]
  
def imprimir_nodos(grafo):
 for x in grafo.nodes():
  print ("nodo ")
  print (x)

g = nx.Graph()
g.add_nodes_from([1,2,3,4,5,6,7,8],visitado=0)


g.add_weighted_edges_from([(1,2,3),(1,3,4),(1,5,8),(1,4,8),(2,4,4),(2,3,4),(3,5,6),(3,4,6),(3,7,5),(3,8,10),(4,8,3),(4,7,8),(5,6,4),(5,7,10),(6,7,6),(7,8,4)])
visitados = []

#pesos = nx.get_edge_attributes(g,'weight')
#for x in pesos:
# print(x)
# print(pesos[x])
vez = 1
nodo_inicio = 1
lista = visitar_nodo(g,nodo_inicio)
print (lista)
#imprimir_nodos(g)





nx.draw_circular(g)
plt.show()

