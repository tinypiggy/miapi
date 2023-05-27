#! /bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from service import xiaoai_from_json

app =  Flask(__name__)

@app.route('/')
def hello_world(data):
    print(data)
    req = xiaoai_from_json(data)
    return 'Hello, World!'