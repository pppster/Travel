from django.urls import path
from . import views

urlpatterns = [
    path(route='article/<int:id>', view=views.article, name='article'),
    path(route='article/create', view=views.article_create, name='article-create'),
    path(route='article-edit/<int:article_id>', view=views.article_edit, name="article-edit"),
    path(route='overview/', view=views.articles_overview, name='article-overview'),
    
]