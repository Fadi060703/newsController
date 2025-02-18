from django.urls import path
from .views import * 

urlpatterns = [
    path( 'articles' , ListCreateArticleView.as_view() , name = 'list-articles' ) ,
    path( 'artilces/<int:pk>' , ArticleDetailView.as_view() , name = 'detail-article' ) , 
]
