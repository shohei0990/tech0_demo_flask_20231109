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


ここでは、アプリケーションのために必要なモジュールをインポートし、ログファイルの名前を設定して、Flaskのインスタンスを生成しています。

## ルートへのアクセス

```python
@app.route('/')
def index():
    return make_top_page_html()

ルート（/）へのアクセスがあった場合に、トップページのHTMLを生成して返します
