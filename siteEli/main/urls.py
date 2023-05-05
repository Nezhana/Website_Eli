from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>', views.song, name='song'),
]
