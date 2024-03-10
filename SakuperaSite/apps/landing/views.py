from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q

def index(request):

    context = {
        "header_title": "Sakupera",
    }

    return render(request, "index.html", context)