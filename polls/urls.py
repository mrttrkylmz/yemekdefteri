from django.urls import path

from . import views




app_name ='polls'
urlpatterns = [
    path('', views.index, name='index'),
    #burası yemekdefteri/polls
    path('<int:question_id>/', views.detail, name='detail'),
    #burası yemekdefteri/polls/1(sorunun idsi)
    path('<int:question_id>/results/', views.results, name='results'),
    #burası yemekdefteri/polls/1/results
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #burası yemekdefteri/polls/1/vote
]
