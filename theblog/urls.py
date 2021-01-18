
from.import views
from django.urls import path
from .views import HomeView , RecipieDetailView, AddRecipieView, UpdateRecipieView, DeleteRecipieView, DeleteSuccess, LikeView, AddCommentView #CommentSuccess
from django.conf.urls.static import static
from django.conf import settings
app_name = 'theblog'

urlpatterns = [

    path('',HomeView.as_view(), name="home"),
    path('recipie/<int:pk>', RecipieDetailView.as_view(), name= "recipie-detail"),
    path('add_recipie/',AddRecipieView.as_view(), name='add-recipie'),
    path('recipie/edit/<int:pk>', UpdateRecipieView.as_view(), name='update-recipie'),
    path('recipie/<int:pk>/delete', DeleteRecipieView.as_view(), name='delete-recipie'),
    path('recipie/deleted', DeleteSuccess, name='delete-success'),
    #path('recipie/commented', CommentSuccess, name='comment-success'),
    path('like/<int:pk>', LikeView, name='like_recipie'),
    path('recipie/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
