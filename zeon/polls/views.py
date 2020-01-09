from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    sobitie = Sobitie.objects.all()
    context = {
        'sobitie': sobitie,
    }
    return render(request,'polls/home.html', context)


