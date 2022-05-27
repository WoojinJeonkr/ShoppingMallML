from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import joblib

def wordcloud_pos():
    pos_dict = joblib.load('C:/Users/hi/Documents/ShoppingMallML/ai/review_pred/pos_dict.pkl')
    words = [n for n in pos_dict if len(n) > 1]
    pos_count = Counter(words)
    wc = WordCloud(font_path='malgun', width=800, height=800,
                   scale=2.0, max_font_size=200,
                   background_color='white', colormap='seismic')
    gen = wc.generate_from_frequencies(pos_count)
    plt.figure()
    plt.imshow(gen, interpolation="bilinear")
    plt.axis('off')
    wc.to_file('static/wordcloud/pos_wordcloud.png')