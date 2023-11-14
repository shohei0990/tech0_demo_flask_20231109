from flask import Flask, request, redirect
import json, os, time, html
from datetime import datetime
from flask import render_template # template engin追加

# firebase活用
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebaseの認証情報を使用して初期化
cred = credentials.Certificate('tech020231115-firebase-adminsdk-861ji-b3420c8933.json') # firebase サービスアカウントのpython 秘密鍵からダウンロードしてね
firebase_admin.initialize_app(cred)

# Firestoreデータベースのインスタンスを取得
db = firestore.client()


# 初期設定　--- (※1)
#logfile = 'bbs_log.json' # 保存先のファイルを指定
logdata = {'lastid': 0, 'logs': []}

app = Flask(__name__) # Flaskを生成

# ルートにアクセスした時に実行する処理を指定 --- (※2)
@app.route('/')
def index():
    load_log() # 追加 : ログデータをロード
    #reversed_logs = reversed(logdata['logs']) # ログデータを逆順にする
    return render_template('index.html', logs=logdata['logs']) # 追加 テンプレートにログデータを渡す

    #return make_top_page_html()

# フォームから投稿した時 --- (※3)
@app.route('/write')
def form_write():
    # 投稿されたデータを取得する --- (※4)
    name = request.args.get('name', '')
    msg = request.args.get('msg', '')
    # パラメータのチェック --- (※5)
    if name == '' or msg == '': return 'パラメータの指定エラー'
    # データを保存 --- (※6)
    append_log({'name': name, 'msg': msg, 'time': time.time()})
    return redirect('/') # トップページに移動

# firebae store DB を読み込む --- (※7)
def load_log():
    logs = []
    docs = db.collection('test').order_by('time', direction=firestore.Query.DESCENDING).stream()
    id_counter = 1  # IDカウンターの初期化
    for doc in docs:
        log = doc.to_dict()
        log['id'] = id_counter  # 連番のIDを割り当て
        logs.append(log)
        id_counter += 1  # IDカウンターをインクリメント
    global logdata
    logdata['logs'] = logs

    # global logdata
    # if os.path.exists(logfile):
    #     with open(logfile, encoding='utf-8') as fp:
    #         logdata = json.load(fp)

# firebae store DB にデータを追記する
def append_log(record):
    db.collection('test').add(record)

# JSONファイルにデータを追記する --- (※8)
# def append_log(record):
#    logdata['lastid'] += 1
#    record['id'] = logdata['lastid']
#    logdata['logs'].append(record) # データを追記
#    with open(logfile, 'w', encoding='utf-8') as fp:
#        json.dump(logdata, fp) # ファイルに書き込む

def make_logs():
    # 書き込まれたログを元にしてHTMLを生成して返す --- (※9)
    s = ''
    for log in reversed(logdata['logs']):
        name = html.escape(log['name']) # 名前をHTMLに変換 --- (※10)
        msg = html.escape(log['msg']) # メッセージをHTMLに変換
        t = datetime.fromtimestamp(log['time']).strftime('%m/%d %H:%M')
        s += '''
        <div class="box">
            <div class="has-text-info">({}) {} さん</div>
            <div>{}</div>
            <div class="has-text-right is-size-7">{}</div>
        </div>
        '''.format(log['id'], name, msg, t)
    return s

#def make_top_page_html():
    # 掲示板のメインページを生成して返す --- (※11)

# 日付のフォーマットを行うカスタムフィルター
@app.template_filter()
def datetimeformat(value, format='%m/%d %H:%M'):
    return datetime.fromtimestamp(value).strftime(format)

if __name__ == '__main__': # Webサーバーを起動 --- (※12)
    # load_log() # ログデータを読み込む
    app.run('127.0.0.1', 8080, debug=True)
