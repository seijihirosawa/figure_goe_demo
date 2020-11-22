from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input_form/', views.input_form, name='input_form'),
    path("result/", views.result, name = "result"),
    path("history/", views.history, name = "history"),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]