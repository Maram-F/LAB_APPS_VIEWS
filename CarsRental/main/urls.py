from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.welcome, name="welcome_view"),
    path("info/", views.about, name="about_view")
]