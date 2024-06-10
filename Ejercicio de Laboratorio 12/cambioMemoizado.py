import time

def coin_change_memo(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        res = coin_change_memo(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    memo[amount] = min_coins
    return memo[amount]

coins = [1, 2, 5, 7, 11]
amount = 26
start_time = time.time()
result = coin_change_memo(coins, amount)
end_time = time.time()
print("Problema del cambio\n")
print(f"Memoizado: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
