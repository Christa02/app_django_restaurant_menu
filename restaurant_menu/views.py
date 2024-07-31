from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuListView(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"


class MealDetailView(generic.DetailView):
    model = Item
    template_name = "meal_detail.html"
