from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile,name = 'profile'),
    path('profiles/)',views.profiles,name='profiles'),
    path('create/', views.create, name='create'),
    path('biz/', views.biz, name='biz'),
    path('hood/', views.hood, name='hood'),
    path('search/', views.search_results, name='search_results'),
    path('post/', views.post, name='post'),
   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
