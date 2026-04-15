from django.urls import path
from . import views

urlpatterns = [
    path('qale/', views.QaleApiView.as_view()),
    path('qale/<int:pk>/', views.QaleDetailApiView.as_view()),
]