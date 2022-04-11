from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id



app.run(port=5001 , debug=True) 
#python server.py 으로 터미널에서 실행
#debug 모드로 하게 되면 새로고침만 해도 페이지 수정됨