from django.urls import path , re_path
from login import views

urlpatterns = [
    path('' , views.index),
    path('signin/' , views.signin)
]
