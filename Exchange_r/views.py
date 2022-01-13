from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Exchange_r/index.html')
'''
def about(request):
    return render(request, 'Exchange_r/about.html')
'''