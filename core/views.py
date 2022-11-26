from django.shortcuts import render

# Create your views here.

def qiymat(request):
    return render(request, 'index.html')
