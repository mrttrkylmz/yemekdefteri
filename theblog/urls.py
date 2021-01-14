
from.import views
from django.urls import path
from .views import HomeView , RecipieDetailView, AddRecipieView, UpdateRecipieView, DeleteRecipieView, DeleteSuccess

app_name = 'theblog'

urlpatterns = [

    path('',HomeView.as_view(), name="home"),
    path('recipie/<int:pk>', RecipieDetailView.as_view(), name= "recipie-detail"),
    path('add_recipie/',AddRecipieView.as_view(), name='add-recipie'),
    path('recipie/edit/<int:pk>', UpdateRecipieView.as_view(), name='update-recipie'),
    path('recipie/<int:pk>/delete', DeleteRecipieView.as_view(), name='delete-recipie'),
    path('recipie/deleted', DeleteSuccess, name='delete-success')
]
