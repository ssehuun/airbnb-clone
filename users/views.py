from django.views import View
from django.shortcuts import render


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass


# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":