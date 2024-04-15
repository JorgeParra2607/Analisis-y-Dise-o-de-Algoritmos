def sqrt_binary_search(x):
    
    # Casos base
    if x == 0 or x == 1:
        return x

    l, r = 0, x // 2
    ans = 0

    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

x = int(input("Ingresa un numero: "))
print("\nLa raiz cuadrada de", x, "es", sqrt_binary_search(x))
