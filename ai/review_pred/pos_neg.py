# 라이브러리 추가
import warnings
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
pos_dict = joblib.load('ai/review_pred/pos_dict.pkl')
neg_dict = joblib.load('ai/review_pred/neg_dict.pkl')
plus_label = joblib.load('ai/review_pred/plus_label.pkl')
tfidf = joblib.load('ai/review_pred/tfidf.pkl')
SA_lr = joblib.load('ai/review_pred/SA_lr.pkl')

def labeling(df, column, i):
    tfidf_list = tfidf
    tfidf_module = tfidf_list[0]
    SA_module = SA_lr
    data = df[column][i]
    data = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", data)
    pn_tfidf = tfidf_module.transform([data])
    predict = SA_module.predict(pn_tfidf)
    if(predict[0] == 1):
        df['review_label'] = df['review_label'].astype(str)
        df.at[i, 'review_label'] = '1F60A'
    else:
        df['review_label'] = df['review_label'].astype(str)
        df.at[i, 'review_label'] = '1F621'
    print(df['review_label'][i])