from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
paw_url = "https://wlsdntyd.pythonanywhere.com"

data = requests.get(f'{url}{token}/setwebhook?url={paw_url}/{token}')
print(data.text)