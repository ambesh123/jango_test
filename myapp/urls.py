from django.urls import path , re_path
from myapp import views

urlpatterns = [
    path('check/', views.check),
    path('check2/', views.check2),
    re_path('viewarticle/(\d+)/', views.viewArticle),
    path('passname/' , views.passName),
    path('nextpage/', views.nextPage),
    path('', views.index),
    path('getpersons/', views.getPersons),
    path('simpleupload/', views.simple_upload),
    path('checkupload/', views.checkUpload),
]
