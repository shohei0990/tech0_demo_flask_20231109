# tech0_demo_flask_20231109

# Flaskによる簡単な掲示板アプリケーション

このコードはFlaskを使って簡単な掲示板アプリケーションを作るためのものです。

## 初期設定 (※1)

```python
from flask import Flask, request, redirect
import json, os, time, html
from datetime import datetime

logfile = 'bbs_log.json' # 保存先のファイル名を設定
logdata = {'lastid': 0, 'logs': []}
app = Flask(__name__) # Flaskアプリケーションを作成
