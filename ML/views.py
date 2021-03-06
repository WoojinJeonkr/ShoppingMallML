# import library
from django.shortcuts import render, redirect
from ML.models import Tag
from ai.review_pred.readall import readAll
from ai.review_pred.wordcloudneg import wordcloud_neg
from ai.review_pred.wordcloudpos import wordcloud_pos
from ai.tag_pred.tag_predict import load_pkl
from ai.review_pred import updatedb, pos_neg, readall

def index1(req):
    return render(req, 'tag/index.html')

def input(req):
    return render(req, 'tag/input.html')

def input2(req):
    data = req.POST
    print('입력한 정보 >> ', data)
    one = Tag(week1=data['week1'], week2=data['week2'], hour=data['hour'],
              gender=data['gender'], age=data['age'], size=data['size'],
              tag_click=data['tag_click'])
    one.save()
    return render(req, 'tag/input2.html')

def search(req):
    return render(req, 'tag/search.html')

def search2(req):
    data = req.POST
    idValue = data['id']
    one = Tag.objects.get(id = idValue)
    print('검색 결과 >> ', one)
    result = {'one' : one}
    return render(req, 'tag/search2.html', context = result)

def output(req, id):
    one = Tag.objects.get(id=id)
    input_data = [one.week1, one.week2, one.hour,
                  one.gender, one.age, one.size,
                  one.tag_click]
    tag_pred = load_pkl(input_data)
    result = {'tag': tag_pred}
    return render(req, 'tag/result.html', context=result)

def index2(req):
    return render(req, 'chart/index2.html')

#시각화처리
#월 평균 구매빈도-3회 이상 (%)의 그래프
def chart1(req):
    #20대~60대까지의 수치를 data에 담음.
    data = [47.475000,48.463462,44.905769,39.793303,39.933024]
    context = {
        'data' : data
    }
    return render(req, 'chart/chart1.html', context)

def chart2(req):
    data = [0.6297657326596233,0.816260909508498,0.6196600826825908,
            0.8171796049609554,0.6669728984841525]
    context = {
        'data' : data
    }
    return render(req, 'chart/chart2.html', context)

def pn_review(req):
    data = req.POST
    review_idx = data['id']
    result = updatedb.update_db(review_idx)
    print(result)
    return redirect('/review/')

def read_all(req):
    review_all = readAll()[0]
    total_count = readAll()[1]
    context = {
        'review_all':review_all,
        'total_count':total_count
    }
    # print(review_all)
    return render(req, 'review/review_all.html', context)

def pn_wordcloud(req):
    wordcloud_pos()
    wordcloud_neg()
    return render(req, 'review/wordcloud_pn.html')