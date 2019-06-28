from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Foodfacttable
from django.urls import reverse

class Foodfactform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Foodfactform, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields["product_name"].widget.attrs["readonly"] = True

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
        instance = get_object_or_404(Foodfacttable, pk=request.POST["product_name"])
        if not request.user.is_anonymous:
            foodform = Foodfactform(data=request.POST, instance=instance)
            if foodform.is_valid():
                foodform.save(commit=True)
    return redirect(reverse("login"))