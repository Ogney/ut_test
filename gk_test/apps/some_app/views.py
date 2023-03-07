from django.shortcuts import render

def some_app(request):       
    return render(request, "some_app/index.html")