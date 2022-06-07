import pymysql

def readAll():
    try:
        conn = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='db_password', # blind db_password
            db='shop2',
            charset='utf8'
        )

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정
        cur = conn.cursor(pymysql.cursors.DictCursor)

        # 3. sql문을 보내보자
        sql = 'select * from review'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql)
        # read인 경우, 커서로 연결 통로에 검색 결과를 꺼내주어야 한다
        row = cur.fetchall()
        # print(row)
        conn.close()
        return row, result
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)
