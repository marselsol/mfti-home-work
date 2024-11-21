from itertools import permutations

GRAPH = [
    [0, 10, 25, 35],
    [10, 0, 20, 30],
    [25, 20, 0, 15],
    [35, 30, 15, 0]
]

START = 2  # Номер стартовой вершины (индексация с 0, вершина 3)


def calculate_cost(path):
    """
    Вычислить стоимость пути.
    """
    cost = 0
    current_city = START

    for next_city in path:
        cost += GRAPH[current_city][next_city]
        current_city = next_city

    cost += GRAPH[current_city][START]  # Возврат в стартовый город
    return cost


def find_shortest_path(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_cost = float('inf')
    best_path = None

    # Генерация всех возможных перестановок оставшихся городов
    for perm in permutations(cities):
        current_cost = calculate_cost(perm)
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = perm

    return min_cost, best_path


if __name__ == "__main__":
    min_cost, best_path = find_shortest_path(GRAPH, START)

    print(f"Минимальная стоимость: {min_cost}")
    print("Маршрут: ", end="")
    print(f"{START + 1} -> ", end="")
    for city in best_path:
        print(f"{city + 1} -> ", end="")
    print(f"{START + 1}")