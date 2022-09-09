# person = {
#     'name' : 'will',
#     'age' : 21,
#     'profeshion': 'Acter'
# }
# person['heigt'] = 180
# person['age'] = 40
# person['planet'] = 'Mars'
# person2 = {'race':'trol'}
# person.update(person2) обновляет словарь
# person.pop('age')удаляет элмент по ключу
# c = person.get('race') возваращает  значения по ключу
# print(person['name']) выводит на экран значения по ключу
# a = person.copy() создает копию словаря 
# person.setdefault(7,'seven') создаете новую пару ключей
# print(person.values()) озвращает значения
# person.keys возвращает ключи

# print(person)

#ЗАДАЧА 101


# suitcase = {
#     'Phone',
#     'книга',
#     'вещи',
#     'тапки',
#     'кальян',
# }
# suitcase.remove('кальян')
# print(suitcase)



# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
#  'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries.('Suriname')
# print(south_american_countries)


#PROBLEM 000

# menu = {
#     'lagman': 120, 
#     'plov': 120, 
#     'borsh': 100,
#     }
# menu2 = {'besh_barmak': 130}
# menu.update(menu2)
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)


# suitcase = []
# count = 0
# while count < 5:
#     b = input('enter suitcase:')
#     count += 1 
#     suitcase.remove(-1)
# print(suitcase) 
# 

# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i * j}\n')   


# dict1 = {
#     '2233':{
#         'name ': 'Alex',
#         'age': '21',
#         'gender': 'M',
#     },
#     '2244': 'Amir',
#     'age': '20',
#     'gender': 'M',
# }
# for value in dict1['2233'].values():
# #     print(value)
# # for value in dict1.values:
# #     print(value)#показывает значения без ключей

# from multiprocessing.sharedctypes import Value


# dict2 = {
#     '2003':{
#         'name': 'Milana',
#         'age': '19',
#         'gender': 'F',
#     },
#     '2002':{
#         'name': 'Amir',
#         'age': '20',
#         'gender': 'M',
#     },
#     '2001':{
#         'name': 'Bektur',
#         'age': '22',
#         'gender': 'M'
#     }
# }
# # print(dict2['2003']['name'])
# # for value in dict2.values():
# #     print(value)

# for key,value in dict2['2002'].items():
# #     print(key,value, end = ' ,')

# a = [5==5,5 > 7]
# print(all(a))#all - возвращает Тру если все знаения верные#

#a = [2,4,6,7,6,4,3]
# n = []
# for i in a:
#     if i % 2 == 0:
#         n.append(True)
#     else:
#         n.append(False)
# print(any(a))
# a.reverse()
# print(a)

# a = eval('2 + 2')
# print(a)


# while True:
#     a = eval(input('>>>>'))
# #     print(a) -СЧИТАЕТ

# a = 10 / 3
# print(round(a,3)) - округляет до выбранного значения

# try:
#     a = [1,2,3,5,6]

# a = []
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# for i in values:
#     try:
#         set(i)
#         a.append(True)
#     except:
#         a.append(False)
# print(all(values))


# a = set()
# for i in range(5):
#     user = int(input("enter your number\n"))
#     a.add(user)
# print(min(a))

# try:
#     a = int(input('Введите цифру a'))
#     b = int(input('Введите цифру b'))
#     print(a/b)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вволите только цифры')

# a = 10
# b = "kak dela"
# try:
#     a + b
#     print











