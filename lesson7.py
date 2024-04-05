#Исключение  try except

# num1 = 9
# num2 = 0 
# print(num1/num2)

# try:
#     num1 = 9
#     num2 = 0 
#     print(num1/num2)

# except ZeroDivisionError:
#     print('На 0 делить не нельза!!!!!')

# while True:
#     try:
#         num1 = int(input("Ведите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         print(f"Результат сложение{num1+num2} ")
#         print(f"Результат вычитание{num1-num2} ")
#         print(f"Результат умножение{num1*num2} ")
#         try:
#             print(f'Результат деление{num1/num2} ')
#         except ZeroDivisionError:
#             print('НА 0 делить ене нельза ')

#     except:
#         print('Ошибка Введите толька числа')

# try:
#         cite = ["Osh", "Bishkek","Talas","Batken"]
#         print(cite.index(Nurdan))
# except:

#         print("Такого индекса нет")

#ЛЯмда функся = Lambda

# sum = lambda num1, num2: num1+num2
# result = sum(7,5)
# print(f"Результат сложение: {}")

# sum = lambda num1, num2: num1+num2
# num1 = int(input("Ведите первое число: "))
# num2 = int(input("Введите второе число: "))
# result = sum(num1,num2)
# print(f"Результат слложение: {result}")

# num_list = [1,2,3,4,5,6,7]
# result = list(map(lambda i: i * 10000000, num_list))
# print(result)

# names = ["Nurai",'Geeks', "Kutbuhan", "Muha","Sabrina"]
# names_list = list(map(lambda i: f"{i} - {len(i)} Букв",names))
# print(names_list)

# print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21, 65, 4677, 86, 46])))

# square = lambda side: side**2
# side_length = 5
# area = square(side_length)
# print(area)

# list_num = [1,-4,6,73,245,7]
# result1 = max(list_num, key=lambda x: x)
# result2 = min(list_num, key=lambda x: x)
# print(result1)
# print(result2)
