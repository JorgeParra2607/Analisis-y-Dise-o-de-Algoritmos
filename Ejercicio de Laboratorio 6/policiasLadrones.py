def policia_y_ladron(arr, k):
    # Obtener el índice más bajo para el policía y el ladrón
    p_index= arr.index('P')
    t_index= arr.index('T')
    assignments = 0
    
    while p_index != -1 and t_index != -1:
        
        # Si la distancia entre el policía y el ladrón es menor o igual a k, incrementar ambos índices
        if abs(t_index - p_index) <= k:
            p_index= arr.index('P', p_index + 1) if 'P' in arr[p_index + 1:] else -1
            t_index= arr.index('T', t_index + 1) if 'T' in arr[t_index + 1:] else -1
            assignments += 1
            
        else:
            # Si la distancia es mayor que k, mover al policía o al ladrón hacia el otro
            if p_index < t_index:
                p_index= arr.index('P', p_index + 1) if 'P' in arr[p_index + 1:] else -1
            else:
                t_index= arr.index('T', t_index + 1) if 'T' in arr[t_index + 1:] else -1
    
    return assignments

# Ejemplo de uso
if __name__ == "__main__":
    arreglo= input("\nIntroduce el arreglo (P para policía, T para ladrón) separado por espacios: ").split()
    k= int(input("\nIntroduce el valor de K: "))
    asignaciones= policia_y_ladron(arreglo, k)
    print("\nNúmero de asignaciones realizadas:", asignaciones)
