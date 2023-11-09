# Flaskによる掲示板アプリケーション

このプロジェクトは、PythonのFlaskフレームワークを使用して簡単な掲示板アプリケーションを作成します。

## 概要

Flaskは、ウェブアプリケーションを作成するための軽量なフレームワークです。これにより、開発者は少ないコードで効率的にアプリケーションを構築することができます。

## 初期設定

```python
from flask import Flask, request, redirect
import json, os, time, html
from datetime import datetime

logfile = 'bbs_log.json' # 保存先のファイル名を設定
logdata = {'lastid': 0, 'logs': []}
app = Flask(__name__) # Flaskアプリケーションを作成
```

ここでは、アプリケーションのために必要なモジュールをインポートし、ログファイルの名前を設定して、Flaskのインスタンスを生成しています。


## ルートへのアクセス

```python
@app.route('/')
def index():
    return make_top_page_html()
```
ルート（/）へのアクセスがあった場合に、トップページのHTMLを生成して返します

## 投稿機能

```python
@app.route('/write')
def form_write():
    # データの取得と保存
    return redirect('/')
```
投稿機能
フォームからのデータを受け取り、ログに記録した後、トップページにリダイレクトします。

## ログデータの読み込みと更新
```python
def load_log():
    # ログファイルの読み込み

def append_log(record):
    # ログデータへの追記
```
ログファイルからデータを読み込む関数と、新しいログエントリを追加する関数です。

## HTML生成
```python
def make_logs():
    # ログからHTMLを生成

def make_top_page_html():
    # トップページのHTMLを生成
```
HTMLコンテンツの生成
掲示板のログエントリからHTMLを生成する関数と、トップページ全体のHTMLを生成する関数です。

## サーバーの起動
アプリケーションが直接実行された際（__name__ == '__main__'）、ログデータを読み込み、Webサーバーを起動します。

```python
Copy code
if __name__ == '__main__':
    load_log()  # ログデータを読み込む
    app.run('127.0.0.1', 8080, debug=True)
```

## JSONログファイルの構造
掲示板アプリケーションで使用するJSONログファイルの例です。

```python
json
Copy code
{
    "lastid": 3,
    "logs": [
        {"name": "●●", "msg": "どうですか？", "time": 1690960437.9061089, "id": 1},
        {"name": "▼▼", "msg": "どうでしょ？", "time": 1698927471.596182, "id": 2},
        {"name": "■■", "msg": "どだい？", "time": 1699434818.6622488, "id": 3}
    ]
}
```
