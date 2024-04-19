def minimo_monedas(V, monedas):
    n= len(monedas)
    resultado= []

    # Lista para almacenar el número mínimo de monedas necesarias
    min_monedas= [0] * (V + 1)

    # Lista para almacenar las monedas utilizadas para cada valor
    monedas_utilizadas= [[] for _ in range(V + 1)]

    # Calcular el número mínimo de monedas para cada valor desde 1 hasta V
    for valor in range(1, V + 1):
        min_monedas[valor]= float('inf')

        for j in range(n):
            if monedas[j] <= valor:

                if 1 + min_monedas[valor - monedas[j]] < min_monedas[valor]:
                    min_monedas[valor]= 1 + min_monedas[valor - monedas[j]]
                   
                    monedas_utilizadas[valor]= monedas_utilizadas[valor - monedas[j]] + [monedas[j]]

    resultado.append(min_monedas[V])

    resultado.append(monedas_utilizadas[V])
    
    return resultado

valores = [2550, 8432, 263]
monedas_disponibles = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

for valor in valores:
    resultado= minimo_monedas(valor, monedas_disponibles)
    print(f"Para el valor {valor} se necesitan {resultado[0]} monedas: {resultado[1]}")
