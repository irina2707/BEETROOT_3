# Завдання 1 - Багатопоточність:
# Завдання: Створіть дві функції:
# 1. Функція, яка виводить "Пінг" кожні 2 секунди
# 2. Функція, яка виводить "Понг" кожну 1 секунду

# Запустіть обидві функції паралельно за допомогою threading.
# Нехай програма працює 6 секунд.

# Очікуваний вивід буде приблизно таким:
# Понг
# Пінг
# Понг
# Понг
# Пінг
# Понг


# import threading
# import time

# # Ваш код тут
# Завдання 2 - Асинхронність:
# Завдання: Створіть три корутини (асинхронні функції, async def):
# 1. get_user(id) - імітує отримання даних користувача (затримка 1 сек)
# 2. get_weather(city) - імітує отримання погоди (затримка 2 сек)
# 3. get_news() - імітує отримання новин (затримка 1 сек)

# Використайте asyncio.gather для паралельного виконання всіх трьох корутин.
# Загальний час виконання має бути приблизно 2 секунди (а не 4).

# Приклад результату:
# Користувач: {"id": 1, "name": "Анна"}
# Погода: {"city": "Київ", "temp": 25}
# Новини: ["Новина 1", "Новина 2"]

# import asyncio
# import time

# async def say_ping():
#     while True:
#         await asyncio.sleep(2)
#         print('ping')

# async def say_pong():
#     while True:
#         await asyncio.sleep(1)
#         print('pong')

# async def main():
#     start_time = time.time()
#     print(f"Started at {time.strftime('%X')}")

   
#     task1 = asyncio.create_task(say_ping())
#     task2 = asyncio.create_task(say_pong())

   
#     await asyncio.sleep(6)


#     task1.cancel()
#     task2.cancel()

#     print(f"Finished at {time.strftime('%X')}")



# asyncio.run(main())

import asyncio
import time

async def get_user(user_id, user_name):
    await asyncio.sleep(1)
    print(f'"id": {user_id}, "name": "{user_name}"')

async def get_weather(city, city_temp):
    await asyncio.sleep(2)
    print(f'"city": "{city}", "temp": {city_temp}')

async def get_news(news_list):
    await asyncio.sleep(1)
    print(news_list)

async def main():
   print(f"Started at {time.strftime('%X')}")
   user_id = 1
   user_name = "Anna"
   city = "Kyiv"
   city_temp = 25
   news_list = ["News 1", "News 2"]
   await asyncio.gather(
        get_user(user_id, user_name),
        get_weather(city, city_temp),
        get_news(news_list)
    )

   print(f"Finished at {time.strftime('%X')}")
asyncio.run(main())
