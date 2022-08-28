import datetime
import requests
from flask import Flask
from flask import Response
from redis_om import get_redis_connection


app = Flask(__name__)

@app.route("/")
def index():
    return "My RSS Cache v0.1"

@app.route("/lic_nttu")
def lic_nttu():
    lib_rss_url = 'https://lic.nttu.edu.tw/search.getService.asp?serviceName=GIP.xdrss&mp=1&ctNodeId=755'
    lib_rss_contents = ''
    redis_conn = get_redis_connection()
    expired = redis_conn.get('lic_nttu_rss_expired')
    now_timestamp = datetime.datetime.now().timestamp()
    status_code = 304
    if expired is not None:
        diff_expired = now_timestamp - float(expired.decode('utf-8'))
    else:
        diff_expired = None
    if redis_conn.get('lic_nttu_rss') is None or diff_expired > 120:
        response = requests.get(lib_rss_url)
        rss_feed = response.text.replace('\r', '')
        redis_conn.set('lic_nttu_rss', rss_feed)
        redis_conn.set('lic_nttu_rss_expired', now_timestamp)
        status_code = 200
        rss_contents = rss_feed
    else:
        rss_contents = redis_conn.get('lic_nttu_rss')

    return Response(rss_contents, status=status_code, mimetype='text/xml')
