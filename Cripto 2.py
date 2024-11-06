import tkinter as tk
import requests
from PIL import Image, ImageTk


def get_crypto_prices():
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin,ripple,cardano&vs_currencies=usd'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            btc_price = data['bitcoin']['usd']
            eth_price = data['ethereum']['usd']
            ltc_price = data['litecoin']['usd']
            xrp_price = data['ripple']['usd']
            ada_price = data['cardano']['usd']

            price_label.config(
                text=f"Bitcoin: ${btc_price:.2f}\nEthereum: ${eth_price:.2f}\nLitecoin: ${ltc_price:.2f}\nRipple: ${xrp_price:.2f}\nCardano: ${ada_price:.2f}"
            )
        else:
            raise ValueError(f'API returned status code {response.status_code}')
    except Exception as e:
        price_label.config(text=f"Произошла ошибка при получении данных: {e}")


root = tk.Tk()
root.title("Курсы криптовалют")
root.geometry("350x300+400+500")

try:
    logo_image = Image.open("лого1.png")
    logo_image = logo_image.resize((80, 80))
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack(pady=10)
except Exception as e:
    print("Ошибка при загрузке логотипа:", e)

price_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
price_label.pack(pady=20)

update_button = tk.Button(root, text="Обновить курсы", command=get_crypto_prices, font=("Arial", 12))
update_button.pack(pady=10)

get_crypto_prices()
root.mainloop()