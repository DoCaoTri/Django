from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_post, name='blog'),
    path('<int:id>/', views.post, name='post')
]