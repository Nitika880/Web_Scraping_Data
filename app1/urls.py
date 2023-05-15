from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.Home),
    path("flipkart-scrap/", views.flipkart_scrapper),
    path("amazon-scrap/", views.amazon_scrapper),
]

