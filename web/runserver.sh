#!/bin/sh

# restore mecab setuped
cp -r /root/mecab-backup/lib/mecab /usr/local/lib/
cp /root/mecab-backup/lib/libmecab.* /usr/local/lib/
cp /root/mecab-backup/bin/* /usr/local/bin/
cp /root/mecab-backup/include/* /usr/local/include/

pip install mecab-python3
gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:5000 --reload app.app:app

