from django.utils import timezone
from django.views.generic import ListView
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


def room_detail(request, pk):
    # print(pk)
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home")) 리다이렉트 하거나 404페이지 띄우거나
        raise Http404()
