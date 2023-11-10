from flask import Flask
from flask import render_template

app = Flask(__name__) # Flask生成

@app.route('/') # ルートにアクセス
def index():
    return 'Hellow World!'

@app.route('/test') # 
def test():
    return "テストページです！"

@app.route('/html') #
def html():
    return html_page()

@app.route('/html2')
def html2():
    my_dict = {
        'insert_something1': 'insert_something1部分です。',
        'insert_something2': 'insert_something2部分です。',
        'test_titles': ['タイトル1', 'タイトル2', 'タイトル3']
    }
    return render_template('index.html', my_dict=my_dict)  # render_templateを使用

def html_page():
    # HTMLページを生成して返す
    return '''<!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>テストWebアプリ</title>
    </head>
    <body>
        <h1>index.html表示してます</h1>
    </body>
    </html>
    '''

if __name__ == '__main__': # Webサーバーを起動 
    app.run('127.0.0.1', 8080, debug=True)