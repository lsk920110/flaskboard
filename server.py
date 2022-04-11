from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h5>debugmode</h5>'

app.run(port=5001 , debug=True) 
#python server.py 으로 터미널에서 실행
#debug 모드로 하게 되면 새로고침만 해도 페이지 수정됨