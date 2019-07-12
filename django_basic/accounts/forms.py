# 사용자에게 입력받을 form태그를 다룰
# 클래스를 작성하는 부분


from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']