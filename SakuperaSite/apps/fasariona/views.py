from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q

def index(request):
    context = {
        "header_title": "Fasa Riona",
    }

    return render(request, 'fasariona/index.html', context)

def dictionary(request):

    word_list = Word.objects.all().order_by('-pk')

    if request.POST:
        query = request.POST.get("simple-query")
        if not query == "":
            word_list = word_list.filter(
                Q(word__icontains=query) |
                Q(desc__note__icontains=query) |
                Q(desc__sentences__sentence__icontains=query) |
                Q(desc__definition__icontains=query)
            )

    context = {
        "word_list" : word_list,
        "header_title": "Dictionary"
    }


    return render(request, "fasariona/dictionary/index.html", context)

def gwiki(request):

    gwiki_list = WikiNote.objects.all().order_by('order_num')

    context = {
        "gwiki_list" : gwiki_list,
        "header_title": "Grammar Wiki"
    }


    return render(request, "fasariona/gwiki/index.html", context)

def gwiki_detail(request, pk):

    gwiki = get_object_or_404(WikiNote, pk=pk)

    context = {
        "gwiki" : gwiki,
        "header_title": gwiki.title
    }


    return render(request, "fasariona/gwiki/detail.html", context)