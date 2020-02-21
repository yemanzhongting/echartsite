from django.shortcuts import render
from django.db import models
from djoncharts.models import AddressInfo,UserInfo,WeiboInfo,coronavirus

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


def adduser (request):
    """ 添加用户数据视图 """
    name=request.POST.get('name')#获取post请求返回的名字
    address=request.POST.get('address')#获取post请求返回的地址
    if request.POST.get('name'):#如果返回有数据
        print('有数据')
        print(request.POST.get('name'))
        try:
            addinfo=AddressInfo.objects.get(add=address)#试图查找地址
        except:#已有地址中找不到则添加新地址
            addinfo=AddressInfo.objects.create(add=address)#添加新的地址
        UserInfo.objects.create(name=name,addinfo=addinfo)#将用户信息加入到用户表中
        # data1.sava()  # 保存修改
    return render(request,'djoncharts/add.html')

def water(request):
    data = coronavirus.objects.all()
    # print(data)
    # data=[1,1,2,3,3,3]
    # data = [{'name': 'wuhan', 'addinfo': 'whu'}]
    print(data.values()[0:20])
    print(type(data))
    context = {'data': data[0:20]}
    # print(context[10])
    # Model.objects.filter(content__contains="条件")
    # context=[1,2,2,1,2,1]
    print(context)
    # context={'data':['zy','wh']}
    return render(request, 'djoncharts/water.html', context)


