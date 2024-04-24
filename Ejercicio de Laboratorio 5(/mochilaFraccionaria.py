def fractional_knapsack(weights, profits, capacity):
    n= len(weights)
    ratios= [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    ratios.sort(reverse=True)
    max_profit= 0

    for ratio, weight, profit in ratios:
        if capacity >= weight:
            max_profit += profit
            capacity -= weight
        else:
            max_profit += ratio * capacity
            break

    return max_profit

weights= list(map(int, input("\nIngrese los pesos de los elementos separados por espacios: ").split()))
profits= list(map(int, input("\nIngrese los valores de los elementos separados por espacios: ").split()))
W = int(input("\nIngrese la capacidad de la mochila: "))

max_profit= fractional_knapsack(weights, profits, W)
print("\nEl beneficio máximo obtenido es:", max_profit)
