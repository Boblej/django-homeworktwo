from django.urls import path
from . import views
from .views import state

urlpatterns = [
    path('', views.index),
    path('state/', state, name='state')
]