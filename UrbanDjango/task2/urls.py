from django.urls import path
from . import views

urlpatterns = [
    path('class-view/', views.ClassBasedView.as_view(), name='class_view'),
    path('function-view/', views.function_based_view, name='function_view'),
]