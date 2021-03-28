from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def all_rooms(request):
    # print(dir(request))
    return render(request, "all_rooms")