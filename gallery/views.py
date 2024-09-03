from django.shortcuts import render

# This will show the list of all available blogs


def productList(req):
    return render(req, 'gallery/productList.html')