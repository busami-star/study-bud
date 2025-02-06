from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


rooms = [
    {'id':1,'name':'busami'},
    {'id':2,'name':'victor'},
    {'id':3,'name':'kisanya'}
]



def home (request):
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
