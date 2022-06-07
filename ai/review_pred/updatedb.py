import pymysql
from ai.review_pred.pos_neg import labeling

def update_db(review_idx):
    review_label = labeling(review_idx)
    print(review_label)
    print(review_idx)
    try:
        conn = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='db_password', # blind db_password
            db='shop2',
            charset='utf8'
        )

        print('연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정
        cur = conn.cursor()

        # 3. sql문을 보내보자
        sql = 'update review set review_label = "' + review_label + '" where review_idx = ' + str(review_idx)
        # 커서로 sql문을 보냄.
        # print('sql>> ', sql)
        result = cur.execute(sql)
        conn.commit()  # update한 것 반영
        # print('sql문 전송 결과>', result)
        conn.close()
        return result # 0: update 실패, 1: update 성공
    except Exception as e:
        print("db 연결 중 에러 발생!!")
        print('에러 정보>> ', e)