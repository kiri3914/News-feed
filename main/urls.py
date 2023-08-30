from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.get_article_by_category, name='get_article_by_category'),
    path('tag/<int:tag_id>/', views.get_article_by_tag, name='get_article_by_tag'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_category/', views.add_category, name='add_category'),
]
