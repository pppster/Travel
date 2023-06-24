from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(route='article/<int:id>', view=views.article, name='article'),
    path(route='article/create', view=views.article_create, name='article-create'),
    path(route='article-edit/<int:article_id>', view=views.article_edit, name="article-edit"),
    path(route='overview/', view=views.articles_overview, name='article-overview'),
    path(route='article-delete/<int:article_id>/', view=views.delete_article, name='delete_article'),
    path(route='image-delete/<str:image_name>/', view=views.delete_image, name='delete_image'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)