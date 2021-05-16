from django.utils import timezone
from django_countries import countries
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # context 안에 템플릿으로 던질 객체가 들어잇음
        context["now"] = timezone.now()  # context에 now를 넣어 template에 던져보자
        return context


class RoomDetail(DetailView):
    """ DetailView Definition """

    model = models.Room
    pk_url_kwarg = "potato"  # url에서 pk로 던져주는 키워드를 potato를 바꿔도 됨(url.py에서 potato 변경요)


def search(request):
    # print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("super_host", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    # print(s_amenities, s_facilities) 유저가 선택한것 확인하기 위함

    # s_room_type 는 front에서 select된걸 말함(선택후 검색시 그대로 보여주기 위해 생성)
    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    ### 검색하기 위한 필터 생성
    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type  # foreign key인 room_type안에서 pk로 필터링

    if price != 0:
        filter_args["price_lte"] = price  # less than or equal

    if guests != 0:
        filter_args["guests_gte"] = guests  # greater than or equal

    if bedrooms != 0:
        filter_args["bedrooms_gte"] = bedrooms

    if beds != 0:
        filter_args["beds_gte"] = beds

    if baths != 0:
        filter_args["baths_gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)
    print(rooms)
    ### end 검색하기 위한 필터 생성
    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
