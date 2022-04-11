from flask import Flask , request ,  redirect

import random


app = Flask(__name__)

nextId = 4
topics = [
    {'id':1,'title':'html','body':'html is...'},
    {'id':2,'title':'css','body':'css is...'},
    {'id':3,'title':'javascript','body':'javascript is...'}

]


def template(contents,content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a><h1>
            <ol>
                {contents}
            </ol>
            <ul>
                <li>{content} <a href="/create/">create</a></li>
            </ul>
        </body>
    </html>    
    '''
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return liTags



@app.route('/')
def index():


    return template(getContents(), '<h2>Welcome</h2>Hello,WEB')  
    

@app.route('/create/', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" placeholder="title" name="title"/></p>
                <p><textarea placeholder="body" name="body"></textarea></p>
                <p><input type="submit" value="create"/></p>
            </form>            
        '''
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId ,'title':title,'body':body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId +=1
        return redirect(url)


    return template(getContents(),content)

@app.route('/read/<int:id>/')
def read(id):

    
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')



app.run(port=5001 , debug=True) 
#python server.py 으로 터미널에서 실행
#debug 모드로 하게 되면 새로고침만 해도 페이지 수정됨