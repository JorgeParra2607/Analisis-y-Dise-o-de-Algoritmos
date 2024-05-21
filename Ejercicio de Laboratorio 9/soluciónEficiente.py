def find_magic_index_binary(arr):
    def binary_search(arr, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return binary_search(arr, start, mid - 1)
        else:
            return binary_search(arr, mid + 1, end)
    
    return binary_search(arr, 0, len(arr) - 1)

# Ejemplo de uso
arr = [-1, 0, 1, 2, 4]
print(find_magic_index_binary(arr))  # Output: 4
