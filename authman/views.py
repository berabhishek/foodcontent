from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Foodfacttable
from django.urls import reverse

class Foodfactform(ModelForm):
    class Meta:
        model = Foodfacttable
        exclude = []

# Create your views here.
def login_page(request, product_name=None):
    foodform = Foodfactform()
    foods = None
    if product_name is not None:
        list_show = False
        try:
            instance = Foodfacttable.objects.get(product_name=product_name)
            foods = Foodfactform(instance=instance)
        except:
            foods = None
    return render(request, "login.html", {
        "foodform": foodform,
        "food":foods
        })

def add_data(request):
    if not request.user.is_anonymous:
        foodform = Foodfactform(request.POST)
        if foodform.is_valid():
            foodform.save(commit=True)
    return redirect(reverse("login"))