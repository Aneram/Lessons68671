phone_book = {}

while True:
    print("\nМеню:")
    print("1. Додати контакт")
    print("2. Пошук контактів")
    print("3. Видалити контакт")
    print("0. Вийти")

    command = input("Введіть команду (0-3): ")

    if command == "1":
        name = input("Введіть ім'я нового контакту: ")
        if name in phone_book:
            print(f"Контакт з ім’ям {name} вже існує: {phone_book[name]}")
        else:
            phone = input("Введіть номер телефону: ")
            phone_book[name] = phone
            print(f"Контакт {name} додано.")

    elif command == "2":
        name = input("Введіть ім'я контакту для пошуку: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print("Контакт не знайдено.")

    elif command == "3":
        name = input("Введіть ім'я контакту для видалення: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт {name} видалено.")
        else:
            print("Контакт не знайдено.")

    elif command == "0":
        print("Вихід із програми.")
        break

    else:
        print("Такої команди немає. Спробуйте ще раз.")
