from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return '''
    <html>
        <head>
            <title>Home page</title>
        </head>
        <body>
            <h1>hello , ''' + user['nickname'] + '''</h1>
        </body>
    </html>
    '''
