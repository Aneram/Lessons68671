# Тобі потрібно створити просту консольну гру, в якій гравець відповідає на запитання.
#
#  Гра буде використовувати оператори if, elif, else для перевірки правильності відповідей.
#
# 1. Програма вітає гравця та пояснює правила гри.
#
# Наприклад, print("Привіт!")
#
# 2. Програма задає гравцеві перше запитання та записує відповідь у змінну. Наприклад:
#
# answer1 = input("Яка столиця України? ")
#
# 3. Перевірка відповіді на перше запитання:
#
# if answer1 == "Київ":
#
# print("Правильно!!!")
#
# else:
#
# print("Неправильно! Правильна відповідь: Київ")
#
# 4. Повторення двох попередніх кроків для усіх запи
print("Привіт! Давай зіграємо в гру. Я задаю тобі питання, а ти повинен правильно на них відповісти")
answer1 = input("Яка столиця України? ")
if answer1 == "Київ":
    print("Правильно!!!")
else:
    print("Неправильно! Правильна відповідь: Київ")
answer2 = input("2+2? ")
if answer2 == "4":
    print("Правильно!!!")
else:
    print("Неправильно! Правильна відповідь: 4")
answer3 = input("Скільки місяців в році? ")
if answer3 == "12":
    print("Правильно!!!")
else:
    print("Неправильно! Правильна відповідь: 12")