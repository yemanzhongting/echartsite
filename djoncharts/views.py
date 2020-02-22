import json

from django.db import models
from djoncharts.models import AddressInfo,UserInfo,WeiboInfo,coronavirus,VirusInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def zhexian(request):
    return render(request, 'djoncharts/zhexian.html')

def show(request):
    data=UserInfo.objects.all()
    print(data)
    # data=[1,1,2,3,3,3]
    data=[{'name':'wuhan','addinfo':'whu'}]

    context = {'data':data}
    # context=[1,2,2,1,2,1]
    print(context)
    # context={'data':['zy','wh']}
    return render(request,'djoncharts/show.html',context)

def adduser(request):
    """ 添加用户数据视图 """
    name = request.POST.get('name')  # 获取post请求返回的名字
    addr = request.POST.get('address')  # 获取post请求返回的地址
    fromarea = request.POST.get('fromarea')  # 获取post请求返回的地址
    temprature = int(request.POST.get('temprature'))  # 获取post请求返回的地址
    tele = request.POST.get('tele')

    #VirusInfo.objects.create(name='aa', addr='aa', fromarea='aa', temprature=3, tele='aa')  # 添加新的地址

    if request.POST.get('tele'):  # 如果返回有数据
        print('有数据')
        print(request.POST.get('name'))
        try:
            VirusInfo.objects.get(addr=addr)  # 试图查找地址
        except:  # 已有地址中找不到则添加新地址
            VirusInfo.objects.create(name=name, addr=addr, fromarea=fromarea, temprature=temprature,tele=tele)  # 添加新的地址

    return render(request, 'djoncharts/add.html')

def virus(request):
    print('@@@@')
    data = request.body
    print(data)
    """ 添加用户数据视图 """
    name=request.POST.get('name')#获取post请求返回的名字
    addr=request.POST.get('address')#获取post请求返回的地址
    fromarea = request.POST.get('fromarea')  # 获取post请求返回的地址
    temprature = request.POST.get('temprature')  # 获取post请求返回的地址
    tele = request.POST.get('tele')

    print('#####')
    print(tele)

    # VirusInfo.objects.create(name='aa', addr='aa', fromarea='aa', temprature=3, tele='aa')  # 添加新的地址

    if request.POST.get('tele'):#如果返回有数据
        print('有数据')
        print(request.POST.get('name'))
        try:
            VirusInfo.objects.get(addr=addr)#试图查找地址
        except:#已有地址中找不到则添加新地址
            VirusInfo.objects.create(name=name,addr=addr,fromarea=fromarea,temprature=temprature,tele=tele)#添加新的地址

    return render(request, 'djoncharts/viradd.html')

from django.shortcuts import render_to_response
import jieba
def ststistic(txt):
    words = jieba.lcut_for_search(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse=True)

    all_list=[]
    for i in range(len(items)):
        all_item = {}
        word, count = items[i]
        if '肺炎' not in word and '全文' not in word:
            all_item['name']=word
            all_item['value'] = count*10
            all_list.append(all_item)

    # print(all_list)
    return all_list[0:200]

# @login_required
def water(request):
    data = coronavirus.objects.all()
    txt=''
    for i in (data.values("txt")[0:500]):
        # print(i)
        txt=txt+' '+i['txt']
    print(type(data))
    # weibo=coronavirus.objects.all()  # 试图查找地址

    context = {'data': data[0:20],'wordcloud':json.dumps(ststistic(txt))}
    return render(request, 'djoncharts/water.html', context)

def eg(request):
    context = {
               'wordcloud': [{'word': '武汉', 'number': 16}, {'word': '汶川', 'number': 15}, {'word': '蔬菜', 'number': 11},
                             {'word': '村民', 'number': 10}, {'word': '12', 'number': 9}, {'word': '爱心', 'number': 8},
                             {'word': '疫情', 'number': 6}, {'word': '我们', 'number': 4}, {'word': '人民', 'number': 4},
                             {'word': '卡车', 'number': 3}, {'word': '三江', 'number': 3}, {'word': '防控', 'number': 3},
                             {'word': '时刻', 'number': 3}, {'word': '汶川县', 'number': 3}, {'word': '一次', 'number': 3},
                             {'word': '运送', 'number': 3}, {'word': '一例', 'number': 3}, {'word': '四川', 'number': 2},
                             {'word': '龙竹村', 'number': 2}, {'word': '故事', 'number': 2}]
               }
    return HttpResponse(json.dumps(context))

# 将数据转化为list来操作(因为别的也不会)
# def jsdaoru(request):
#     wheelsList = Wheel.objects.all()
#     name = list(Wheel.objects.values_list('name', flat=True))
#     data = list(Wheel.objects.values_list('trackid', flat=True))
#     return render(request,'axf/js_daoru.html',{"wheelsList":wheelsList,"name":name,"data":data})






