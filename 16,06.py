my_list = []

film = []

print("🎬 Вітаємо! Це програма 'Список фільмів'.")
print("Ви можете додавати фільми, видаляти їх та передивлятись весь список.")
print("Створіть свою колекцію улюбленого кіно! 🍿\n")
print("Оберіть дію:")
print("1. Додати фільм")
print("2. Показати всі фільми у списку")
print("3. Видалити фільм")
choice = input("Ваш вибір (1-3): ")
if choice == 1 :
    film = input("Введіть назву фільму, який хочете додати: ")
    my_list.append("")
    print(f"Фільм '{film}' додано до списку.")
if choice == 2 :
    if my_list:
        print("Ваш список фільмів:")
        for movie in my_list:
            print("-", movie)
    else:
        print("Список фільмів порожній.")
if choice == 3 :
    film = input("Введіть назву фільму, який хочете видалити: ")
    if film in my_list:
        my_list.remove(film)
        print(f"Фільм '{film}' видалено.")
    else:
        print(f"Фільм '{film}' не знайдено у списку.")
else:
    print("Невірний вибір. Спробуйте ще раз.")


