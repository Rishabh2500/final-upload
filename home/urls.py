from django.contrib import admin
from django.urls import path, include
from home.views import StudentView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.index, name="HOME"),
   path('movies/', views.movies, name="movies"),
   path('streams/', views.streams, name="streams"),
   path('events/', views.events, name="events"),
   path('plays/', views.plays, name="plays"),
   path('sports/', views.sports, name="sports"),
    path('students/', StudentView.as_view(), name='student-list')
]