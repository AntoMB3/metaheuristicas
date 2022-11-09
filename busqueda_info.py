import json
import random
import math

fil = open('ciudades_info.json')
data = json.load(fil)
fil.close()

def choosen_citie(ciudades):
    s = 0
    for i in ciudades:
        print(str(s) + " " + i)
        s += 1
    res = int(input())
    return res

def hill_climbing(origen,destino,ciudades):
    recorrido = []
    city = ""
    actual = ciudades[origen]
    pasada = ""
    retornos = -2
    if(origen == destino):
        print("Ya estas en la ciudad :D")
        pass
    recorrido.append(ciudades[origen])
    temp_avoid = 0
    while(True):
        if (actual == pasada):
            temp_avoid += 1
        if(city == ciudades[destino]):
            return recorrido

        posibilidades = list(data['cities'][actual])
        po_temp = list()
        for i in posibilidades:
            if i not in recorrido:
                po_temp.append(i)
        posibilidades = po_temp
        maxi = 10000
        pasada = actual
        if(len(posibilidades) > 0):
            retornos = -2
            for p in posibilidades:
                if(data['cities'][actual][p] < maxi):
                    maxi = data['cities'][actual][p]
                    city = p
            recorrido.append(city)
            actual = city
        if(temp_avoid > 10):
            actual = recorrido[retornos]
            retornos -= 1
            temp_avoid = 0

def sol_inicial(origen,destino,ciudades):
    peso = 0
    recorrido = []
    city = ""
    actual = ciudades[origen]
    pasada = ""
    retornos = -2
    recorrido.append(ciudades[origen])
    temp_avoid = 0
    while(True):
        if (actual == pasada):
            temp_avoid += 1
        if(city == ciudades[destino]):
            return recorrido,peso

        posibilidades = list(data['cities'][actual])
        po_temp = list()
        for i in posibilidades:
            if i not in recorrido:
                po_temp.append(i)
        posibilidades = po_temp
        pasada = actual
        if(len(posibilidades) > 0):
            retornos = -2
            cantidad_posibilidades = len(posibilidades)
            elegido = random.randint(0,cantidad_posibilidades-1)
            city = posibilidades[elegido]
            recorrido.append(city)
            peso += data['cities'][actual][city]
            actual = city
        if(temp_avoid > 10):
            actual = recorrido[retornos]
            retornos -= 1
            temp_avoid = 0
            
def recocido(origen,destino,ciudades,t0,t1):
    random.seed(t1)
    k,p,i,a = 0,0,0,0
    T = t0
    sol,peso = sol_inicial(origen,destino,ciudades)
    while(T > t1):
        while(k < 20 and a < 5):
            sol_alternativa,peso_alternativo = sol_inicial(origen,destino,ciudades)
            if(peso_alternativo < peso):
                sol = sol_alternativa
                peso = peso_alternativo
            else:
                p = random.random()
                division = (peso - peso_alternativo)/(T)
                if(p < pow(math.e,division)):
                    sol = sol_alternativa
                    peso = peso_alternativo
                    a += 1
            k += 1
        
        T = T - 100
        k = 0
        a = 0
    return sol,peso

    
ciudades = list(data["cities"])
print("Elige lugar origen")
origen = choosen_citie(ciudades)
print("Elige lugar Destino")
destino = choosen_citie(ciudades)

#recorrido_voraz = hill_climbing(origen,destino,ciudades)
#print(recorrido_voraz)

recorrido_recocido,peso = recocido(origen,destino,ciudades,800,300)
print(str(recorrido_recocido) + " Peso : " + str(peso))