import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin,ripple,cardano&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()

    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    ltc_price = data['litecoin']['usd']
    xrp_price = data['ripple']['usd']
    ada_price = data['cardano']['usd']

    price_label.config(
        text=f"Bitcoin: ${btc_price}\nEthereum: ${eth_price}\nLitecoin: ${ltc_price}\nRipple: ${xrp_price}\nCardano: ${ada_price}")

root = tk.Tk()
root.title("Курсы криптовалют")
root.geometry("350x300+400+500")
try:
    logo_image = Image.open("лого1.png")
    logo_image = logo_image.resize((80, 80))
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.image = logo_photo  # Чтобы избежать сборщика мусора
    logo_label.pack(pady=10)
except Exception as e:
    print("Ошибка при загрузке логотипа:", e)

# Метка для отображения курсов криптовалют
price_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
price_label.pack(pady=20)

# Кнопка для обновления курсов
update_button = tk.Button(root, text="Обновить курсы", command=get_crypto_prices, font=("Arial", 12))
update_button.pack(pady=10)

# Запуск окна
get_crypto_prices()  # Получаем курсы сразу при запуске
root.mainloop()