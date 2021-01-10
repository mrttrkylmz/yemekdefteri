from django.urls import path

from . import views



app_name = 'recipies'
urlpatterns = [
    path('', views.index, name='index'),
    #burası yemekdefteri/recipies
    path('<int:recipies_id>/', views.detail, name='detail'),
    #burası yemekdefteri/recipies/1(recipienin idsi)
    path('<int:recipies_id>/vote_results/', views.results, name='results'),
    #burası yemekdefteri/recipies/1/vote_results
    path('<int:question_id>/upvote/', views.upvote, name='upvote'),
    #burası yemekdefteri/polls/1/upvote
    path('<int:question_id>/downvote/', views.downvote, name='downvote')
    #burası yemekdefteri/polls/1/downvote

    
]
