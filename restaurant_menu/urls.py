from django.urls import path
from . import  views


urlpatterns = [
    path('', views.MenuListView.as_view(), name="home"),
    path('meal_details/<int:pk>', views.MealDetailView.as_view(), name="meal_details")
]