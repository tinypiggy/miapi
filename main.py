#! /bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response, request
from service import xiaoai_from_json
import time
# from service.xiaoai import XiaoAIActionProperty

app =  Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def callbackFromMi():
    print('X-Xiaomi-Date = {}'.format(request.headers.get('X-Xiaomi-Date')))

    data = request.get_data(as_text=True)
    print('data = {}'.format(data))

    req = xiaoai_from_json(data)

    resp = make_response('Hello, World!')
    resp.headers['x-original-host'] = 'api.tinypig.top'
    resp.headers['X-Xiaomi-Date'] = time.asctime(time.localtime(time.time()))
    return resp