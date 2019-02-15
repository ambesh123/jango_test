
from django.urls import path , re_path
from myapp import views

urlpatterns = [
    path('check/', views.check),
    path('check2/', views.check2),
    re_path('viewarticle/(\d+)/', views.viewArticle),
    path('', views.index),
]
