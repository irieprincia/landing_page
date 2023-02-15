from django.shortcuts import render


def index(request):

    template='symbioll/index.html'
    
    return render(request, template)

# Create your views here.
