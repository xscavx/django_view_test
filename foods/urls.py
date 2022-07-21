from django.urls import path

from . import views

urlpatterns = [path("foods", views.foods, name="foods")]
