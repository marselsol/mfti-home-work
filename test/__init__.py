import pandas as pd

# Загрузка данных
Cars = pd.read_csv('Electric_Car.csv')

# Убедимся, что нет пропусков в PriceEuro, заменяя NaN значением 0 (если требуется)
Cars['PriceEuro'] = Cars['PriceEuro'].fillna(0)

# Группировка по бренду и вычисление средней цены
Carsgroupby = Cars.groupby('Brand', as_index=False)['PriceEuro'].mean()

# Просмотр результата
print(Carsgroupby)

# Проверка суммы для прохождения теста
print(Carsgroupby['PriceEuro'].sum())
