from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import joblib

def wordcloud_neg():
    neg_dict = joblib.load('C:/Users/hi/Documents/ShoppingMallML/ai/review_pred/neg_dict.pkl')
    words = [n for n in neg_dict if len(n) > 1]
    neg_count = Counter(words)
    wc = WordCloud(font_path='malgun', width=800, height=800,
                   scale=2.0, max_font_size=200,
                   background_color='white', colormap='summer')
    gen = wc.generate_from_frequencies(neg_count)
    plt.figure()
    plt.imshow(gen, interpolation="bilinear")
    plt.axis('off')
    wc.to_file('static/wordcloud/neg_wordcloud.png')