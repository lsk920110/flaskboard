from flask import Flask , request ,  redirect



app = Flask(__name__)

nextId = 4
topics = [
    {'id':1,'title':'html','body':'html is...'},
    {'id':2,'title':'css','body':'css is...'},
    {'id':3,'title':'javascript','body':'javascript is...'}

]


def template(contents,content, id=None):#id 기본값 None
    contextUI = ''    
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}">update</a></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a><h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
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
        return template(getContents(),content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId ,'title':title,'body':body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)



@app.route('/read/<int:id>/')
def read(id):
    title= ''
    body = ''    
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}',id)






@app.route('/update/<int:id>/', methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        print('수정page'+request.method)
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" placeholder="title" name="title" value="{title}"/></p>
                <p><textarea placeholder="body" name="body">{body}</textarea></p>
                <p><input type="submit" value="update"/></p>
            </form>            
        '''
        return template(getContents(),content)
    elif request.method == 'POST':
        print('수정기능'+request.method)

        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)










app.run(port=5001 , debug=True) 
#python server.py 으로 터미널에서 실행
#debug 모드로 하게 되면 새로고침만 해도 페이지 수정됨    