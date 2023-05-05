from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='coop_home'),
    path('done', views.coop_done, name='coop_done'),
]
