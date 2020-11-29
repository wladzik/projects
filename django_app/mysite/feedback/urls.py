from django.urls import path

from . import views

app_name = "feedback"  # in html you can do "feedback:name" pattern, creating url
urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('her', views.feedback_form, name='feedback_form'),
]