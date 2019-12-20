from flask import Flask, render_template, request
from decouple import config
import random
import requests
app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"


@app.route('/')
def hello():
    return "Hello world"

@app.route('/write')
def write():
    return render_template('write.html') 

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

@app.route(f'/{token}', methods=["POST"])
def telegram():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    if text == "안녕":
        return_text = "안녕하세요"
    elif text == "로또":
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6))
    else :
        return_text = "지금 지원하는 채팅은 안녕입니다"

    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={return_text}')
    return "ok", 200


if __name__==("__main__"):
    app.run(debug=True)