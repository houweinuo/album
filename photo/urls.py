# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 15:31
# @Author  : HWN
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from photo.views import HomeView, UploadView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
]
