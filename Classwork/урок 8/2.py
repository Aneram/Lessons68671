phone_book = {}

print("1.Додати контакт")
print("2.Пошук контактів")
print("3.Видалити контакт")
kontact = input("Ведіть, що хочете зробити!")
if kontact == "1":
    name = input("Ведіть ім'я нового контакту")
    if name in phone_book:
        print(f"Контакт з ім’ям {name} вже існує: {phone_book[name]}")
    else:
        phone = input("Ведіть номер контакту, який треба додати")
        phone_book[name] = phone
        print(f"Контакт {name} додано.")
if kontact == "2":
    print("Ведіть назву контакту, який треба знайти")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Контакт не знайдено.")
if kontact == "3":
    print("Ведіть назву контакту, який хочете видалити")
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} видалено.")
    else:
        print("Контакт не знайдено.")
else:
    print("Такої команди немає")


