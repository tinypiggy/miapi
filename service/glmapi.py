#! /bin/env python
# -*- coding:utf-8 -*-

import requests
import json

# curl -X POST v4.tinypig.top:10080      -H 'Content-Type: application/json'      -d '{"prompt": "你好", "history": []}'
def getAnswer(prompt):
    data = {"prompt": prompt, "history": []}

    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}

    ## post的时候，将data字典形式的参数用json包转换成json格式。
    response = requests.post(url='http://v4.tinypig.top:10080', headers=headers, data=json.dumps(data))
    answer = json.loads(response.text)
    return answer['response']

if __name__ == '__main__':
    print(getAnswer('梅西和C罗谁更好'))
        