from django.urls import path
from .views import homePage, HomeView, AboutPage


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
]
