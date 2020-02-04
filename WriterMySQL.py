import pymysql
import json

class Writer :
    # MariaDB의 접속 정보를 config.json로부터 받아온다.
    def __init__(self):
        global config
        with open('conf/config.json', 'r') as f:
            config = json.load(f)

    # Database와 연결
    def connect(self):
        global conn, cursor
        conn = pymysql.connect(host=config['MYSQL']['HOST'], port=config['MYSQL']['PORT'], user=config['MYSQL']['USER'],
                             passwd=config['MYSQL']['PW'], db=config['MYSQL']['DBNAME'], charset='utf8')
        cursor = conn.cursor()
        print("[DB] CONNECT")

    # Database와 연결 해제
    def disconnect(self):
        global conn
        conn.close()
        print("[DB] DISCONNECT")
