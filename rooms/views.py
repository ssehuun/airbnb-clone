from django.utils import timezone
from django_countries import countries
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models, forms


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
    form = forms.SearchForm
    return render(request, "rooms/search.html", {"form": form})
