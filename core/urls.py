from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),  # path는 class가 아닌 함수만 가짐
]
