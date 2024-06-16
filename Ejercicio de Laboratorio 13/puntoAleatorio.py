import random
import math

# Función para generar un punto aleatorio dentro de un cuadrado [-1, 1] x [-1, 1]
def generate_point():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return (x, y)

# Función para verificar si un punto está dentro de un círculo unitario
def is_inside_circle(point):
    x, y = point
    return x**2 + y**2 <= 1

# Generar y contar puntos
def simulate_points(num_points):
    inside_points = 0
    outside_points = 0
    
    for _ in range(num_points):
        point = generate_point()
        if is_inside_circle(point):
            inside_points += 1
        else:
            outside_points += 1
            
    return inside_points, outside_points

# Función para representar visualmente los puntos y el círculo usando texto
def print_visualization(inside_points, outside_points, total_points):
    inside_ratio = inside_points / total_points
    outside_ratio = outside_points / total_points
    print(f"Total de puntos: {total_points}")
    print(f"Puntos dentro del círculo: {inside_points} ({inside_ratio:.2%})")
    print(f"Puntos fuera del círculo: {outside_points} ({outside_ratio:.2%})")

    grid_size = 20  # Tamaño de la cuadrícula para visualización
    for y in range(grid_size, -grid_size - 1, -1):
        row = ""
        for x in range(-grid_size, grid_size + 1):
            point_x = x / grid_size
            point_y = y / grid_size
            if point_x**2 + point_y**2 <= 1:
                row += "O"
            else:
                row += "."
        print(row)

# Número de puntos a generar
total_points = 1000

# Simular puntos y obtener conteos
inside_points, outside_points = simulate_points(total_points)

# Imprimir visualización
print_visualization(inside_points, outside_points, total_points)
