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
Copy code
@app.route('/')
def index():
    return make_top_page_html()
```
投稿機能
フォームからのデータを受け取り、ログに記録した後、トップページにリダイレクトします。

## ログの読み込みと追加
```python
Copy code
@app.route('/write')
def form_write():
    # ...
    return redirect('/')
```
ログデータの読み込みと更新
ログファイルからデータを読み込む関数と、新しいログエントリを追加する関数です。

## HTML生成
```python
Copy code
def load_log():
    # ...

def append_log(record):
    # ...
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
