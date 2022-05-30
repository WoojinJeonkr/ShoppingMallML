import pymysql

# 데이터 베이스 연결 및 데이터 불러오기
def db_read(review_idx):
    try:
        conn = pymysql.connect(
            host='amazon rds endpoint addr',
            port=3306,
            user='root',
            password='database pwd',
            db='shop',
            charset='utf8'
        )

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'select * from review where review_idx = %s order by review_rgstdate limit 1'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql, review_idx)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchone() #row하나만 꺼내
        conn.close()
        return row
    except Exception as e:
        print("db 연결 중 에러 발생!!")
        print('에러 정보>> ', e)