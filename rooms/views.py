from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def all_rooms(request):
    # print(dir(request))
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
