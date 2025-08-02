import customtkinter as ctk
import requests

# Отримання актуального курсу з CoinGecko API
def get_exchange_rates():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,tether",
        "vs_currencies": "uah"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        print("📊 Актуальні курси:")
        print(f"BTC → UAH: {data['bitcoin']['uah']}")
        print(f"ETH → UAH: {data['ethereum']['uah']}")
        print(f"USDT → UAH: {data['tether']['uah']}")
        print("UAH: 1")
        return {
            "BTC": data["bitcoin"]["uah"],
            "ETH": data["ethereum"]["uah"],
            "USDT": data["tether"]["uah"],
            "UAH": 1.0  # для зручності
        }
    except Exception as e:
        print("Помилка при отриманні курсу:", e)
        return {
            "BTC": 0,
            "ETH": 0,
            "USDT": 0,
            "UAH": 1
        }

# Налаштування вікна
app = ctk.CTk()
app.title("Конвертер криптовалют")
app.geometry("400x300")

# Заголовок
title_label = ctk.CTkLabel(app, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

# Поле для вводу суми
entry_amount = ctk.CTkEntry(app, placeholder_text="Введи суму")
entry_amount.pack(pady=10)

# Вибір валют
from_currency_var = ctk.StringVar(value="BTC")
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
from_currency_menu.pack(pady=5)

to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu = ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
to_currency_menu.pack(pady=5)

# Кнопка конвертації
def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        rates = get_exchange_rates()

        amount_in_uah = amount * rates[from_currency]
        converted_amount = amount_in_uah / rates[to_currency]

        result_label.configure(
            text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}"
        )
    except ValueError:
        result_label.configure(text="❌ Введи число")
    except Exception as e:
        result_label.configure(text=f"❌ Помилка: {e}")

convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

# Результат конвертації
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

# Запуск програми
app.mainloop()