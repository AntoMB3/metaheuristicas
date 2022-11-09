import json

fil = open('ciudades.json')
data = json.load(fil)
fil.close()

def choosen_citie(ciudades):
    s = 0
    for i in ciudades:
        print(str(s) + " " + i)
        s += 1
    res = int(input())
    return res
    
def busqueda_anchura(origen,destino,ciudades):
    cola = []
    recorrido = []
    if(origen == destino):
        print("Ya estas en la ciudad :D")
        pass
    for i in data["cities"][ciudades[origen]]:
        cola.append(i)
    recorrido.append(ciudades[origen])
    while(len(cola) != 0):
        actual = cola[0]
        if (actual in recorrido):
            cola.pop(0)
        else:
            actual_index = ciudades.index(actual)
            recorrido.append(actual)
            if(actual == ciudades[destino]):
                print("Conseguido!")
                return recorrido
            cola.extend(data['cities'][ciudades[actual_index]])
            #Quitar repetidos
            cola = list(set(cola))
            cola.pop(0)

def busqueda_profundidad(origen,destino,ciudades):
    cola = []
    recorrido = []
    if(origen == destino):
        print("Ya estas en la ciudad :D")
        pass
    for i in data["cities"][ciudades[origen]]:
        cola.append(i)
    recorrido.append(ciudades[origen])
    while(len(cola) != 0):
        actual = cola[0]
        if (actual in recorrido):
            cola.pop(0)
        else:
            actual_index = ciudades.index(actual)
            recorrido.append(actual)
            if(actual == ciudades[destino]):
                print("Conseguido!")
                return recorrido
            for i in data['cities'][ciudades[actual_index]]:
                cola.insert(0,i)
            #Quitar repetidos
            cola = list(set(cola))
            cola.pop(0)

ciudades = list(data["cities"])

print("Elige lugar origen")
origen = choosen_citie(ciudades)
print("Elige lugar Destino")
destino = choosen_citie(ciudades)
recorrido = busqueda_anchura(origen,destino,ciudades)
print("Recorrido obtenido por anchura: ")
print(recorrido)

recorrido_profundidad = busqueda_profundidad(origen,destino,ciudades)
print("Recorrido obtenido por profundidad: ")
print(recorrido_profundidad)
