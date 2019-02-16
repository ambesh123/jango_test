from django.urls import path , re_path
from isp import views

urlpatterns = [
    path('' , views.index),
    path('sortbyprice/' , views.sortbyprice),
    path('sortbyrating/' , views.sortbyrating),
    path('getdesc/' , views.getDesc),
]
