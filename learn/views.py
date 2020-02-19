# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
import json
from .algorithm_base import xianjinliu


# Create your views here.
def index1(request):
    return render(request, 'demo.html')


def run(request):
    params = request.POST
    # print params
    model = xianjinliu(params)
    final = model.run_model()
    return render(request, 'demo.html', {"x": json.dumps(final)})

def chr(request):
    # Create your views here.

    years = range(1997, 2018)
    # return render(request, 'year_test.html', {"data": years})

    return render(request, 'chr.html',{"data": years})

def xr(request):
    return render(request,'indexr.html')

#def news_report(request):
#  article_listing = []   
#  for article_list in List.objects.all():   
#    article_dict = {}   
#    article_dict[&apos;news_object&apos;] = article_list   
#    article_dict[&apos;item_count&apos;] = article_list.item_set.count()   
#    article_dict[&apos;items_title&apos;] = article_list.title  
#    article_dict[&apos;items_complete&apos;] = article_list.item_set.filter(completed=True).count()   
#    article_dict[&apos;percent_complete&apos;] =  
#         int(float(article_dict[&apos;items_complete&apos;]) / article_dict[&apos;item_count&apos;] * 100)   
#    article_listing.append(article_dict)   
# return render_to_response(&apos;news_report.html&apos;, { &apos;article_listing&apos;: article_listing })   