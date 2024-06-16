import random

# Definimos el sistema de ecuaciones como funciones
def equations(x, y, z, t):
    eq1 = x + 2*y - z + 3*t + 8
    eq2 = 2*x + 2*z - t - 13
    eq3 = -x + y + z - t - 8
    eq4 = 3*x + 3*y - z + 2*t + 1
    return (eq1, eq2, eq3, eq4)

# Función para calcular el error total
def total_error(solution):
    x, y, z, t = solution
    eq1, eq2, eq3, eq4 = equations(x, y, z, t)
    return abs(eq1) + abs(eq2) + abs(eq3) + abs(eq4)

# Rango de valores aleatorios
range_values = range(-5, 6)
best_solution = None
min_error = float('inf')

# Iteramos hasta 10 millones de veces
for i in range(10_000_000):
    # Generamos una solución aleatoria
    solution = (random.choice(range_values), random.choice(range_values),
                random.choice(range_values), random.choice(range_values))
    
    # Calculamos el error total de esta solución
    error = total_error(solution)
    
    # Si encontramos una solución exacta, la imprimimos y salimos
    if error == 0:
        best_solution = solution
        break
    
    # Si esta solución es la mejor encontrada hasta ahora, la guardamos
    if error < min_error:
        min_error = error
        best_solution = solution

# Imprimimos la mejor solución encontrada
print("Mejor solución encontrada:", best_solution)
print("Error total:", min_error)
