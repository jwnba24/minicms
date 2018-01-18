# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from models import Article,Column
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'news/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })

def column_detail(request,column_slug):
    c = Column.objects.get(slug=column_slug)
    return render(request,'news/column.html',{'column': c})

#django.shortcuts.redirect 是一个比较方便的函数(详情)：
#
# 1. 传递一个网址的时候，跳转到网址：redirect('http://www.ziqiangxuetang.com') 跳转到自强学堂首页
#
# Django 1.7 版本开始可以接收相对路径：redirect('/django/') 跳转到 Django 教程栏目 下
#
# 2. 传递一个 Model object 的时候，自动调用object的 get_absolute_url 函数获取网址，上面就是一个这样的例子。

def article_detail(request, pk, article_slug):
    article = Article.objects.get(id=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article': article})