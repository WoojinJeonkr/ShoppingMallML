# import library
from django.shortcuts import render, redirect
from ML.models import Tag
from ai.tag_predict import load_pkl

def index(req):
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
