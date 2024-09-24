#��Ʒ �ɵ�ȡapi��ǰ�˶Խ� ʵ�ֶԻ�����
import _thread as thread
import os
import time
import base64

import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket
#import openpyxl
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

#ǰ�˻�ȡ
import time
#import serial


from flask import  request, Flask, jsonify
from flask_cors import CORS, cross_origin
import pymysql
app = Flask(__name__)
cors = CORS(app)


# ���ݿ�����
DB_HOST = 'localhost'
DB_USER = 'root'
###@@@此处密码应与上文您账号密码相同，请更改↓  @@@
DB_PASSWORD = 'your_password'
###@@@此处密码应与上文您账号密码相同，请更改↑  @@@
DB_NAME = 'xinghuo'

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)


class Ws_Param(object):
    # ��ʼ��
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    # ����url
    def create_url(self):
        # ����RFC1123��ʽ��ʱ���?
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # ƴ���ַ���
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # ����hmac-sha256���м���
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # ������ļ�Ȩ�������Ϊ�ֵ�
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # ƴ�Ӽ�Ȩ����������url
        url = self.gpt_url + '?' + urlencode(v)
        # �˴���ӡ����������ʱ���url,�ο���demo��ʱ���ȡ���Ϸ���ӡ��ע�ͣ��ȶ���ͬ����ʱ���ɵ�url���Լ��������ɵ�url�Ƿ�һ��
        return url


# �յ�websocket����Ĵ���?
def on_error(ws, error):
    print("### error:", error)


# �յ�websocket�رյĴ���
def on_close(ws):
    print("### closed ###")


# �յ�websocket���ӽ����Ĵ���
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, query=ws.query, domain=ws.domain))
    ws.send(data)


def gen_params(appid, query, domain):
    """
    ͨ��appid���û������������������?
    """

    data = {
        "header": {
            "app_id": appid,
            "uid": "1234",
            # "patch_id": []    #����΢��ģ�ͣ���Ӧ���񷢲����resourceid
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.5,
                "max_tokens": 4096,
                "auditing": "default",
            }
        },
        "payload": {
            "message": {
                "text": [{"role": "user", "content": query}]
            }
        }
    }
    return data

nana=' '
# �յ�websocket��Ϣ�Ĵ���
def on_message(ws, message):
    # print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'�������?: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]

        global nana
        nana+=content
        print(content,end='')
        if status == 2:
            #print("#### �رջỰ")
            ws.close()



miao='  '


@app.route('/senddata', methods=['POST'])  # �����û���Ϣ�����ݿ�
def test():
    try:

        global miao
        data = request.get_json()
        askk = data.get('askk')
        miao = askk + ',����85����ѧ83������80��������ѧ70��Ӣ��60�֡�'

        appid = "e6429c25"
        api_secret = "NGI5M2QyZjQyMGE5ODJiNjY4MjhkYWU1"
        api_key = "249d53d20fb062816e7c5ebb1a89b048"
        gpt_url = "wss://spark-api.xf-yun.com/v3.5/chat"
        domain = "generalv3.5"
        query = ""

        wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
        websocket.enableTrace(False)
        wsUrl = wsParam.create_url()

        ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
        ws.appid = appid
        ws.query = miao + query
        ws.domain = domain
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        global nana
        answer = nana
        ask = askk


        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO aa(ask,answer) VALUES (%s, %s)"
            cursor.execute(sql, (ask, answer))
            # �ύ����
            connection.commit()


            connection.close()
        return nana


    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/shuaxin', methods=['GET'])  # �����û���Ϣ�����ݿ�
def shuaxin():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM aa"
            cursor.execute(sql)
            results = cursor.fetchall()

            fanhui = []
            for row in results:
                fanhui.append({
                    'id': row[0],
                    'ask': row[1],
                    'answer': row[2]
                })

            connection.close()

            return jsonify(fanhui)

    except pymysql.MySQLError as e:
        return jsonify({'error': str(e)}), 500



if __name__ == "__main__":
    ###此处ip为与前端连接同一热点后的ip，请根据具体情况进行更改�?
    app.run(host='192.xxx.xx.xxx', port=5000)
    ###此处ip为与前端连接同一热点后的ip，请根据具体情况进行更改�?

