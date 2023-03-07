from django.shortcuts import render

def menus(request):       
    return render(request, "menus/menu_tree.html")