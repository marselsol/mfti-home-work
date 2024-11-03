import requests

def task1():
    print("Задание 1: Получение данных из публичного API")
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}\n")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
    print("-" * 50)

def task2():
    print("Задание 2: Работа с параметрами запроса")
    city = input("Введите название города: ")
    api_key = '97fb9953a1cb21e58f59ec1888cd0036'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Текущая температура в городе {city}: {temp}°C")
        print(f"Описание погоды: {description}")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
    print("-" * 50)

def task3():
    print("Задание 3: Создание и обработка POST-запросов")
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        'title': 'Заголовок моего поста',
        'body': 'Это тело моего поста.',
        'userId': 1
    }

    response = requests.post(url, json=payload)
    if response.status_code == 201:
        post = response.json()
        print(f"Создан пост с ID: {post['id']}")
        print(f"Содержимое поста:")
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}")
    else:
        print(f"Ошибка при создании поста: {response.status_code}")
    print("-" * 50)

def task4():
    global response
    print("Задание 4: Обработка ошибок и работа с данными")
    url = 'https://jsonplaceholder.typicode.com/invalid_endpoint'  # Специально неверный URL для проверки ошибки
    payload = {
        'title': 'Заголовок моего поста',
        'body': 'Это тело моего поста.',
        'userId': 1
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 400:
            print("Ошибка 400: Неверный запрос.")
        elif response.status_code == 404:
            print("Ошибка 404: Ресурс не найден.")
        else:
            print(f"HTTP ошибка: {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка запроса: {err}")
    else:
        post = response.json()
        print(f"Создан пост с ID: {post['id']}")
        print(f"Содержимое поста:")
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}")
    print("-" * 50)

def main():
    task1()
    task2()
    task3()
    task4()

if __name__ == "__main__":
    main()
