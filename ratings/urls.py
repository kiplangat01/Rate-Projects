from . import views 
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
  path('', views.index, name='index'),
  path('rating/(?P<pk>\d+)$',views.Rateproject,name="rate_project"),
  path('project/<post>', views.project, name='project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)