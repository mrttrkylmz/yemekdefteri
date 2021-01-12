
#from.import views
from django.urls import path
from .views import HomeView , RecipieDetailView

app_name = 'theblog'

urlpatterns = [

    path('',HomeView.as_view(), name="home"),
    path('recipie/<int:pk>', RecipieDetailView.as_view(), name= "recipie-detail"),
]
