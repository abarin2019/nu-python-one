import requests
import json
from flask import Flask
from datetime import datetime


def get_currencies_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['Date'], list(data['Valute'].values())


app = Flask(__name__)


def create_html(date, currencies):
    date = datetime.fromisoformat(date).strftime('%d.%m.%Y')
    text = f'<h1>Курс валют</h1>'
    text += f'<h2>Дата: {date}</h2>'
    text += '<table>'
    text += '<tr>'
    for _ in currencies[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in currencies:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    date, currencies = get_currencies_list()
    return create_html(date, currencies)


if __name__ == "__main__":
    app.run()