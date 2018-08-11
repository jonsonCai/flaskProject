import cx_Oracle

from flask import render_template, flash, redirect

from app import app
from app.froms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'Jhon'},
            'body': 'Beautiful day!!'
        },
        {
            'author': {'nickname:': 'Susan'},
            'body': 'The Avengers moving was so cool'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    else:
        return render_template('login.html', form=form, title='Sign In', providers=app.config['OPENID_PROVIDERS'])

@app.route('/aaa', methods=['GET'])
def aaa():
    return '123890'

@app.route('/getUser', methods=['GET', 'POST'])
def getUser():
    conn = cx_Oracle.connect('SCOTT', 'abc123', '127.0.0.1/AkiDemo')
    cursor = conn.cursor()
    msg = cursor.var(cx_Oracle.STRING)
    status = cursor.var(cx_Oracle.NUMBER)
    # cursor.callproc('user_table.query_user_for_cursor', [1, status, msg, re_cur])
    cursor.execute('select * from users')

    # result_status, result_msg = status.getvalue(), msg.getvalue()
    result_str = ''
    rows = cursor.fetchall()
    print(rows.count)
    for row in rows:
        print(row)
        result_str = result_str + '  ' + str(row) + '<br>'
    cursor.close()
    conn.close()
    # rows = re_cur.fetchall()
    # for row in rows:
    #     print(row)
    # cursor.close()
    return result_str


