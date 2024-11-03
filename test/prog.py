import pandas as pd

# Загрузка данных
Cars = pd.read_csv('Electric_Car.csv')

# Группировка по бренду и вычисление средней цены с округлением
Carsgroupby = Cars.groupby('Brand', as_index=False)['PriceEuro'].mean().round(2)

# Проверка суммы
print(Carsgroupby)
print(Carsgroupby['PriceEuro'].sum())
