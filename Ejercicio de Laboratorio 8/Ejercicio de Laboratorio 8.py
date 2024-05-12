# Algoritmo utilizando recursividad plana
def count_ways_recursive(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways_recursive(n - 1) + count_ways_recursive(n - 2) + count_ways_recursive(n - 3)

# Algoritmo utilizando memoización
def count_ways_memoization(n, memo={}):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n in memo:
        return memo[n]
    else:
        memo[n] = count_ways_memoization(n - 1, memo) + count_ways_memoization(n - 2, memo) + count_ways_memoization(n - 3, memo)
        return memo[n]

def test_cases():
    
    # Caso 1: Escalera con 5 escalón
    n1 = 5
    print("Número de escalones:", n1)
    print("Recursividad plana:", count_ways_recursive(n1))
    print("Memoización:", count_ways_memoization(n1))
    print("--------------------------------------")

    # Caso 2: Escalera con 7 escalones
    n2 = 7
    print("Número de escalones:", n2)
    print("Recursividad plana:", count_ways_recursive(n2))
    print("Memoización:", count_ways_memoization(n2))
    print("--------------------------------------")

    # Caso 3: Escalera con 10 escalones
    n3 = 10
    print("Número de escalones:", n3)
    print("Recursividad plana:", count_ways_recursive(n3))
    print("Memoización:", count_ways_memoization(n3))
    print("--------------------------------------")

    # Caso 4: Escalera con 12 escalones
    n4 = 12
    print("Número de escalones:", n4)
    print("Recursividad plana:", count_ways_recursive(n4))
    print("Memoización:", count_ways_memoization(n4))
    print("--------------------------------------")

test_cases()
