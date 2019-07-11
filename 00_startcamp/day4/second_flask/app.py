import datetime
import requests
import json
from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/add')
def add():
    return render_template('add.html')
    # add.html 숫자2개 받고 더함


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)
    # num1 = request.args.get('no1')
    # num2 = request.args.get('no2')
    # num3 = int(num2)+int(num1)
    # return render_template('result.html', num1=num1, num2=num2, num3=num3)  # result.html 결과 보여줌


@app.route('/receive', methods=['POST'])
def receive():
    data = request.form.get('msg')
    stock = Stock(data, token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
    company_name = stock['companyName'] 
    latest_price = stock['iexRealtimePrice']
   
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=WXMbETdKM85UpFQpuZ8Sf4QcrUQyKaM5&searchdate=20190710&data=AP01'
    response = requests.get(url).text
    money = json.loads(response)
    dal_kor = money['ttb']
    print(dal_kor)
    k_price = float(l_price)*float(dal_kor)

    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price,
        k_price=k_price
        )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    # return f'ssafy 2기 1학기 종료일까지 {left.days}일 남았습니다.'
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3 파라블럼',
        '라이온 킹'
    ]
    return render_template('boxoffice.html', movies=top_5)


if __name__ == '__main__':
    app.run(debug=True)
