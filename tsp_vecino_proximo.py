import matplotlib.pyplot as plt
import networkx as nx
import sys
import numpy as np



def visitar_nodo(grafo,nodo):
    
    nodo_nuevo = ""
    tupla = ()
    menor_peso = 11111.0
   # pesos = nx.get_edge_attributes(grafo,'weight')
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
     ## print("nodo ",nodo," vecinos ",grafo.neighbors(nodo))
      for y in pesos:
        n1 = y[0]
        n2 = y[1]
      
      
         
        if (x==n1 or x==n2) and (nodo==n1 or nodo==n2) and x not in visitados:
             #print(n1,",",n2," peso ",pesos[y])
            
             if vecinos_visitados < (len(grafo.nodes())-1):
               if x == nodo_inicio:
                 continue
               
               else:
                 
                # print ("el peso es :",pesos[y])
                 if pesos[y] < menor_peso:
                    #print("el menor a cambiado")
                    menor_peso = pesos[y]
                    nodo_nuevo = x  
       
              
             else:
              nodo_nuevo = x          
                 
             
           
         
            
    
    
    
          
    
    
    
    #nodo = nodo_vecino(tupla,nodo)
    print("---------------")
    print("el nodo visitado es")
    print(nodo_nuevo)
    grafo.node[nodo_nuevo]['visitado'] = 1
    #print("el nodo se marco como visitado")
    #print(grafo.node[nodo_nuevo]['visitado'])
    #nada = str(input())
    visitados.append(nodo_nuevo)
    print("nodos visitados")
    print(visitados)
    
    if todos_visitados(grafo) == False:
     print("hola")
     visitar_nodo(grafo,nodo_nuevo)
    else:
       visit = nx.get_node_attributes(grafo,'visitado')
       #print(visit)
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
  
def agregar_pesos(grafo,n_nodos,matriz):
  pesos = []
  for i in range(n_nodos):
    for j in range(n_nodos):
      if j==i:
       continue
      distancia = np.sqrt((int(matriz[j][1]) - int(matriz[i][1]))**2) + np.sqrt((int(matriz[j][2]) - int(matriz[i][2]))**2) 
      pesos.append((matriz[i][0],matriz[j][0],distancia))
  grafo.add_weighted_edges_from(pesos)
  return pesos
  
  
        
def llenar_grafo(grafo,n_nodos,archivo):
 
 archi = open(archivo,"r")
 matriz = [[0]*3 for i in range(n_nodos)]
 linea = archi.readline()
 for i in range(n_nodos):
   nodo = linea.split(" ")
   num = nodo[0]
   px = nodo[1]
   py = nodo[2]
   matriz[i][0] = num
   matriz[i][1] = px
   matriz[i][2] = py
   linea = archi.readline()
 
 lista_nodos = []
 for i in range(n_nodos):
   lista_nodos.append(matriz[i][0])
 grafo.add_nodes_from(lista_nodos,visitado=0)  
 return matriz       

g = nx.Graph()
#g.add_nodes_from([1,2,3,4,5,6,7,8],visitado=0)


#g.add_weighted_edges_from([(1,2,3),(1,3,4),(1,5,8),(1,4,8),(2,4,4),(2,3,4),(3,5,6),(3,6,5),(3,4,6),(3,7,5),(3,8,10),(4,8,3),(4,7,8),(5,6,4),(5,7,10),(6,7,6),(7,8,4)])
matriz_archivo = llenar_grafo(g,280,"g1.txt")
visitados = []
#print(matriz_archivo)
matriz_pesos = agregar_pesos(g,280,matriz_archivo)
#print(matriz_pesos)
pesos = nx.get_edge_attributes(g,'weight')
print("los pesos-------------------------------------------------------------")
print(pesos)
vez = 1
nodo_inicio = "1"
"""for x in g.nodes():
  print (x)"""
lista = visitar_nodo(g,nodo_inicio)
print (lista)
print(visitados)
print("numero de nodos :",len(visitados))
#imprimir_nodos(g)





nx.draw_random(g)
plt.show()
