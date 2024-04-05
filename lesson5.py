# # Словарь
# # user = ['Nurdan', 'Geeks']"
# student = {'name': "Nurdan", 'age': 14, 'hobby': "Football" , 'city':"osh"}

# #Создаётся фигурными  скопками Всегда в себе ключ и значение
# #МЫ не можем использовать индексы Используйте ключ для получение 
# print(student["name"])
# print(student["hobby"])
# print(student)
# student['cityy'] = "osh"
# print(student)
# student['age'] = 19
# print(student)
# # student.pop('hobby')
# # print(student)

# del student['hobby']
# print(student)

# name = (f"Привет меня {student},мне {student}. Я живу в городе {student}. ")
# print(student["name"])
# print(student["age"])
# print(student["city"])
# print("name")
# print(f"Привет меня завут {student['name']}, мне {student['age']}. Я живу в городе {student['city']} ")

# key = student.keys() #ЧТобы показать толька ключи
# print(key)

# values = student.values()
# print(values)

# result = {"num1": 12,23 : 43}
# print(result)


#set frozenset
#Создаётся с помащю {} скобок Не име.т  структуры и порядка и поетому меняются местами нне  можем использовать индексы и срезы
#set изменяемый
#frozenset не изменяемый

# user = {"NUrdan", "Sabrina", "Geeks", "Islam", "Musi", "Beka"}
# print(user)
# # print(user[0])
# user.add("Nurai")
# print(user)
# user.remove("Musi")
# print(user)
# user.discard("Nurbolot")
# print(user)

# user = frozenset(["NUrbolot","NUrdan", "Sabrina", "Geeks", "Islam", "Musi", "Beka"])
# print(user)

import random

users_healsc = 5
bot_hehealsc = 5
while True:
    if users_healsc == 0:
        print("конец вы проиграли")
    elif bot_hehealsc == 0:
        print("бот проиграл")
    else:
        bot = random.choice(["Кaмень","Ножницы","Бумага"])
        users = input("Введите ваш выбор: ")
        if users == "Камень":
            if bot == "Камень":
                print(f"Ничья у вас {users_healsc} попытак у бота: {bot_hehealsc}")
            elif bot == "Ножницы":
                bot_hehealsc -=1
                print(f"вы выйграли у вас: {users_healsc} у бота {bot_hehealsc}") 
            elif bot == "Бумага":
                users_healsc -=1
                print(f"Вы проиграли у {users_healsc} у бота {bot_hehealsc}")
        elif users == "Ножницы":
            if bot == "Ножницы":
                print(f"Ничья у вас {users_healsc} попытак у бота: {bot_hehealsc}")
            elif bot == "Бумага":
                bot_hehealsc -=1
                print(f"вы выйграли у вас: {users_healsc} у бота {bot_hehealsc}") 
            elif bot == "Камень":
                users_healsc -=1
                print(f"Вы проиграли у {users_healsc} у бота {bot_hehealsc}")
        elif users == "Бумага":
            if bot == "Бумага":
                print(f"Ничья у вас {users_healsc} попытак у бота: {bot_hehealsc}")
            elif bot == "Камень":
                bot_hehealsc -=1
                print(f"вы выйграли у вас: {users_healsc} у бота {bot_hehealsc}") 
            elif bot == "Ножницы":
                users_healsc -=1
                print(f"Вы проиграли у {users_healsc} у бота {bot_hehealsc}")
        else:
            print("Не верный вариант ведите снова")
