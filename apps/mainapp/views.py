from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def page2(request):
    return render(request, 'mainapp/page2.html')
