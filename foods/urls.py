from django.urls import path

from foods import views

urlpatterns = [
    path("foods/", views.FoodsList.as_view(), name="foods list"),
]
