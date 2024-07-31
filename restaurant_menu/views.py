from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuListView(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {"meals": ["Pizza", "Pancake"],
                   "ingredients": ["dough"]}
        return context


class MealDetailView(generic.DetailView):
    model = Item
    template_name = "meal_detail.html"
