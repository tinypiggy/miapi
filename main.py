#! /bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response, request
from service import xiaoai_from_json, xiaoai_response
import time
# from service.xiaoai import XiaoAIActionProperty
import logging
from logging import FileHandler

app =  Flask(__name__)
handler = logging.FileHandler('/var/log/miapi/app.log')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))
app.logger.addHandler(handler)

@app.route('/', methods=['POST', 'GET'])
def callbackFromMi():
    app.logger.info('X-Xiaomi-Date = {}'.format(request.headers.get('X-Xiaomi-Date')))
    app.logger.info('Authorization = {}'.format(request.headers.get('Authorization')))

    req_data = request.get_data(as_text=True)
    app.logger.info('req_data = {}'.format(req_data))

    # req = xiaoai_from_json(data)

    resp_data = {
        "version":"1.0",
        "response":{
            "to_speak":
            {
                "type": 0,
                "text": "刘晨逸是个大笨蛋"
            },
            "not_understand": False
        },
        "is_session_end": False
    }
    resp = make_response(xiaoai_response(resp_data))
    resp.headers['x-original-host'] = 'api.tinypig.top'
    resp.headers['X-Xiaomi-Date'] = time.asctime(time.localtime(time.time()))
    return resp