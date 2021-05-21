from django.urls import path
from . import views

urlpatterns = [
    path('', views.toSubmit_view),
    path('submit/', views.submit_view),
]