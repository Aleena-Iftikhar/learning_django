from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("I am jango. This is my FIRST jango project.")


def otherPage(request):
    return HttpResponse('This is another page.')

def htmlpage(request):
    people = [
        {'name': "Aleena", 'age': 20},
        {'name': "Anisa", 'age': 25},
        {'name': "Akram", 'age': 40},
    ]
    return render(request, "index.html", context={'People':people})    # data from backend to frontend