from . import views 
from django.urls import path, include,path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
  path('', views.index, name='index'),
  path('new_Project/',views.add_Project,name = 'project'),
  path('search/', views.searchproject, name='search'),
  path('projects/<int:id>',views.projects,name = 'projects'),
  # path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
  path('rate/<id>/',views.rate,name = 'rate')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)