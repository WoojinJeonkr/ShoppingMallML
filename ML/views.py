# import library
from django.http import HttpResponse
from django.shortcuts import render
from ML.models import Tag
from ai.tag_pred.tag_predict import load_pkl

def start(req):
    return HttpResponse('<center><h3>시작페이지</h3><hr color=red>' +
                        '<a href=/tag/>태그 예측 사이트</a><br>' +
                        '<a href=/label/>긍정/부정 판단 사이트</a><br>'+
                        '<a href=/chart/>차트 확인 사이트</a></center>'
                        )

def index1(req):
    return render(req, 'tag/index.html')

def index2(req):
    return render(req, 'review/index2.html')

def index3(req):
    return render(req, 'chart/index3.html')

def chart2(req):
    data = [0.6297657326596233,0.816260909508498,0.6196600826825908,
            0.8171796049609554,0.6669728984841525]
    context = {
        'data' : data
    }
    return render(req, 'chart/chart2.html', context)

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
