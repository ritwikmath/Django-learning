from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "property/index.html")

def contact(request):
    return render(request, "property/contact.html")