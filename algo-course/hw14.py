from scipy.optimize import linprog
import numpy as np

supply = [100, 200]  # Запасы на складах C1 и C2
demand = [50, 100, 75, 75]  # Потребности магазинов M1, M2, M3, M4
costs = [
    [4, 3, 5, 6],  # Затраты C1 -> M1, M2, M3, M4
    [8, 2, 4, 7]   # Затраты C2 -> M1, M2, M3, M4
]

num_supply = len(supply)
num_demand = len(demand)

c = np.array(costs).flatten()

A_supply = np.zeros((num_supply, num_supply * num_demand))
for i in range(num_supply):
    for j in range(num_demand):
        A_supply[i, i * num_demand + j] = 1

b_supply = supply

A_demand = np.zeros((num_demand, num_supply * num_demand))
for j in range(num_demand):
    for i in range(num_supply):
        A_demand[j, i * num_demand + j] = 1

b_demand = demand

A_eq = np.vstack([A_supply, A_demand])
b_eq = np.hstack([b_supply, b_demand])

result = linprog(c, A_eq=A_eq, b_eq=b_eq, method='highs')

if result.success:
    print("Минимальная стоимость перевозок:", result.fun)
    x = result.x.reshape((num_supply, num_demand))
    print("Распределение груза по складам и магазинам:")
    for i in range(num_supply):
        for j in range(num_demand):
            print(f"Склад {i+1} -> Магазин {j+1}: {x[i, j]:.0f} единиц")
else:
    print("Не удалось найти оптимальное решение")
