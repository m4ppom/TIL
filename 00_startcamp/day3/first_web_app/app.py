from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/hi')
# def hi():
#     return 'HI'


# @app.route('/get_lotto/<int:num>')
# def get_lotto


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


@app.route('/hello/<name>')  # var routing
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')  # var routing
def pick_lunch(count):
    menus = {
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '군만두',
        '사천탕면',
        '마라탕',
        '마라샹궈'
    }
    picks = random.sample(menus, count)
    return str(picks)  # 튀어나갈 애


@app.route('/cube/<int:number>')
def cube(number):
    s3 = number**3

    return str(s3)

if __name__ == '__main__':
    app.run(debug=True)
