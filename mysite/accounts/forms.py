# forms
from django import forms
from django.contrib.auth.models import User

# 회원가입 model form
class SignupForm(forms.ModelForm):
    # Meta class :  Meta 클래스는 ModelForm 클래스에 메타데이터를 제공하기 위해 쓰인다
    class Meta:
        model = User # 장고에서 제공하는 User 모델 사용
        fields = ['username', 'email', 'password']

# 로그인 model form
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']