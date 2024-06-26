from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.my_form_view, name='my_form'),
]