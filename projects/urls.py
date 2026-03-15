from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list),
    path('<slug:slug>/', views.project_detail),
]