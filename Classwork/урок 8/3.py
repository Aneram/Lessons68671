phone_book = {}

print("1. Додати контакт")
print("2. Пошук контактів")
print("3. Видалити контакт")
kontact = input("Введіть, що хочете зробити (1, 2 або 3): ")

if kontact == "1":
    name = input("Введіть ім'я нового контакту: ")
    if name in phone_book:
        print(f"Контакт з ім’ям {name} вже існує: {phone_book[name]}")
    else:
        phone = input("Введіть номер телефону: ")
        phone_book[name] = phone
        print(f"Контакт {name} додано.")

elif kontact == "2":
    name = input("Введіть ім'я контакту для пошуку: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Контакт не знайдено.")

elif kontact == "3":
    name = input("Введіть ім'я контакту для видалення: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} видалено.")
    else:
        print("Контакт не знайдено.")

else:
    print("Такої команди немає.")
