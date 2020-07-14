from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")

    class Meta:
        model=User

        fields = ("username", "email") # email 필드를 Meta 클래스에 추가

        # fields = ["username","email","password1","password2"]


# UserCreationForm은 is_valid() 함수로 폼 체크시 위 3개 속성을 필수값으로 체크한다. 그리고 "비밀번호1"과 "비밀번호2"의 값이 같은지를 체크하고 비밀번호의 값이 비밀번호 생성규칙에 맞는지를 검증한다.