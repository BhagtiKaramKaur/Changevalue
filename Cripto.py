import tkinter as tk
import requests

# Функция для получения курсов криптовалют
def get_c_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

# Функция для обновления меток с курсами
def update_prices():
    prices = get_c_prices()
    bitcoin_price.set(f"Bitcoin (BTC): ${prices['bitcoin']['usd']}")
    ethereum_price.set(f"Ethereum (ЕТН): ${prices['ethereum']['usd']}")
    ripple_price.set(f"Ripple (XRP): ${prices['ripple']['usd']}")
    root.after(60000, update_prices)  # Обновление каждые 60 секунд

# Создание основного окна приложения
root = tk.Tk()
root.title("Курсы криптовалюты")

# Переменные для хранения цен
bitcoin_price = tk.StringVar()
ethereum_price = tk.StringVar()
ripple_price = tk.StringVar()

# Создание меток для отображения цен
tk.Label(root, textvariable=bitcoin_price, font=("Snap ITC", 16)).pack(pady=10)
tk.Label(root, textvariable=ethereum_price, font=("Snap ITC", 16)).pack(pady=10)
tk.Label(root, textvariable=ripple_price, font=("Snap ITC", 16)).pack(pady=10)

# Первичное получение курсов и их отображение
update_prices()