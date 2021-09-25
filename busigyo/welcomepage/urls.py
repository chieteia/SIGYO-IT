from django.urls import path
from welcomepage import views

app_name='welcomepage'

urlpatterns = [
    path('', views.index, name='index'),
    #path('masuno', views.index2, name='aaa'),
]
