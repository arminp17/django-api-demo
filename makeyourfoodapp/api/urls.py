from django.urls import path
from . import views

urlpatterns = [
    path('post', views.AppmodelDetail.as_view())
]