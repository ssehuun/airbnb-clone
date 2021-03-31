from math import ceil
from django.shortcuts import render
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)  # page 숫자가 입력되지 않았을때 1페이지로 설정
    content_size = 10
    limit = content_size * page
    offset = limit - content_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / content_size)
    return render(
        request,
        "rooms/home.html",
        {
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
