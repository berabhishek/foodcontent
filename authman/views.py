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
    list_show = True
    if product_name is not None:
        list_show = False
        instance = Foodfacttable.objects.get(product_name=product_name)
        foods = Foodfactform(instance=instance)
    else:
        foods = Foodfacttable.objects.all()
    return render(request, "login.html", {
        "foodform": foodform,
        "list_show":list_show,
        "foods":foods
        })

def add_data(request):
    foodform = Foodfactform(request.POST)
    if foodform.is_valid():
        foodform.save(commit=True)
    return redirect(reverse("login"))