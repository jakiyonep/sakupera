from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q

def index(request):

    word_list = Word.objects.all().order_by('-pk')
    print(len(word_list))

    if request.POST:
        query = request.POST.get("simple-query")
        if not query == "":
            word_list = word_list.filter(
                Q(word__icontains=query) |
                Q(desc__note__icontains=query) |
                Q(desc__sentences__sentence__icontains=query) |
                Q(desc__definition__icontains=query)
            )

    print(len(word_list))
    context = {
        "word_list" : word_list,
    }


    return render(request, "fasariona/dictionary/index.html", context)
