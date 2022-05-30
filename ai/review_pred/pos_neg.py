# 라이브러리 추가
import warnings

from ai.review_pred.connectdb import db_read

warnings.filterwarnings(action='ignore')
import re
import pandas as pd
import numpy as np
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 모듈 불러오기
pos_dict = joblib.load('/home/ubuntu/projects/shoppingmall/ai/review_pred/pos_dict.pkl')
neg_dict = joblib.load('/home/ubuntu/projects/shoppingmall/ai/review_pred/neg_dict.pkl')
plus_label = joblib.load('/home/ubuntu/projects/shoppingmall/ai/review_pred/plus_label.pkl')
tfidf = joblib.load('/home/ubuntu/projects/shoppingmall/ai/review_pred/tfidf.pkl')
SA_lr = joblib.load('/home/ubuntu/projects/shoppingmall/ai/review_pred/SA_lr.pkl')

# 하나의 내용에 대한 라벨(긍정/부정에 따른) 붙이는 함수
def labeling(i):
    tfidf_list = tfidf
    tfidf_module = tfidf_list[0]
    SA_module = SA_lr
    row = db_read(i)
    p_row = list(row)
    data = p_row[3]
    data = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", data)
    pn_tfidf = tfidf_module.transform([data])
    predict = SA_module.predict(pn_tfidf)
    if(predict[0] == 1):
        p_row[7] = '1F60A'
        return p_row[7]
    else:
        p_row[7] = '1F621'
        return p_row[7]