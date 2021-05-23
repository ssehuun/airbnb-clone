from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data  # clean함수를 쓰면 clened_data를 return 해야함
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong")
                )  # 해당 필드에서 에러가 난다는 알려주기 위해 add_error 사용
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
