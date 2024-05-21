def find_magic_index_linear(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

# Ejemplo de uso
arr = [-1, 0, 1, 2, 4]
print(find_magic_index_linear(arr))  # Output: 4
