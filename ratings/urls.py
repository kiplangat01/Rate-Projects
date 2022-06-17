from . import views 
from django.urls import path, include,path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.searchproject, name='search'),
  path('project/<int:id>',views.project,name = 'project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)