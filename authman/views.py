from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Foodfacttable
from django.urls import reverse
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict

class Foodfactform(ModelForm):
    def make_disable(self):
        for field in self.fields.keys():
           self.fields[field].widget.attrs["readonly"] = True
    
    class Meta:
        model = Foodfacttable
        exclude = []

# Create your views here.
def login_page(request, product_name=None):
    foodform = Foodfactform()
    foods = None
    if request.method == "POST":
        product_name = request.method["product_name"]

    if product_name is not None:
        try:
            instance = Foodfacttable.objects.get(product_name=product_name)
            if request.user.is_anonymous:
                foods = Foodfactform(instance=instance)
                foods.make_disable()
            else:
                if request.method == "POST":
                    foods = Foodfactform(instance=instance, data=request.POST)
                    foods.save(commit=True)
                else:
                    foods = Foodfactform(instance=instance)
        except:
            foods = None
    return render(request, "login.html", {
        "foodform": foodform,
        "food":foods
        })

def add_data(request):
    if request.method == "POST":
        if not request.user.is_anonymous:
            try:
                instance = get_object_or_404(Foodfacttable, pk=request.POST["product_name"])
                foodform = Foodfactform(data=request.POST, instance=instance)
            except Http404:
                foodform = Foodfactform(data=request.POST)
            if foodform.is_valid():
                foodform.save(commit=True)
    return redirect(reverse("login"))

def table_api(request, product_name=None):
    try:
        my_object = get_object_or_404(Foodfacttable, pk=product_name)
        return JsonResponse(model_to_dict(my_object))
    except Http404:
        return JsonResponse({"status": "error", "message":"The product_name is incorrect"})