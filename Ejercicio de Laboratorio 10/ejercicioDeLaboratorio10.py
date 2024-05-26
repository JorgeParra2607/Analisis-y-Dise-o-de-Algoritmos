from collections import deque

def is_goal(state):
    # El objetivo es tener 4 litros en la jarra de 5 litros
    return state[0] == 4

def get_successors(state):
    successors = []
    x, y = state
    
    # Jarra de 5 litros (X) y jarra de 3 litros (Y)
    jarra_5 = 5
    jarra_3 = 3
    
    # Llenar la jarra de 5 litros
    successors.append((jarra_5, y))
    # Llenar la jarra de 3 litros
    successors.append((x, jarra_3))
    # Vaciar la jarra de 5 litros
    successors.append((0, y))
    # Vaciar la jarra de 3 litros
    successors.append((x, 0))
    # Verter de 5 litros a 3 litros
    pour_5_to_3 = min(x, jarra_3 - y)
    successors.append((x - pour_5_to_3, y + pour_5_to_3))
    # Verter de 3 litros a 5 litros
    pour_3_to_5 = min(y, jarra_5 - x)
    successors.append((x + pour_3_to_5, y - pour_3_to_5))
    
    return successors

def solve_jug_problem():
    # Estado inicial (0, 0)
    start_state = (0, 0)
    # Cola para BFS
    queue = deque([(start_state, [])])
    # Conjunto para estados visitados
    visited = set()
    
    while queue:
        (current_state, path) = queue.popleft()
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        if is_goal(current_state):
            return path + [current_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                queue.append((successor, path + [current_state]))
    
    return None

solution = solve_jug_problem()

if solution:
    print("Solución encontrada:")
    for step in solution:
        print(step)
else:
    print("No se encontró solución")
