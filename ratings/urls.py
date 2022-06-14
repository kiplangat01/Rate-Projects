from . import views 
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
  path('', views.index, name='index'),
  path('rating/(?P<pk>\d+)$',views.Rateproject,name="rate_project"),
  path('upload/',views.Upload_Project,name="upload_project"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)