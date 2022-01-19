from django import forms
from .models import Application


class RegisterForm(forms.Form):
    email = forms.EmailField(label='이메일', error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'})
    password = forms.CharField(label='비밀번호', min_length=6, max_length=20, widget=forms.PasswordInput) #widget:UI구현할때 어떻게 구현할것인지 forms.PasswordInput: 가려지게끔 쓰겠다
    password_confirm = forms.CharField(label='비밀번호 확인', min_length=6, max_length=20, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean() #아무리 clean이라는 method를 덮어쓰더라도

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm") #전달받은 값을 하나씩 꺼냄
        if password and password_confirm:#둘다 입력이 되었을때
            if password != password_confirm: #만약 다르다면
                raise forms.ValidationError({
                    "password_confirm": ["2개의 비밀번호가 일치하지 않습니다."]
                })

        return cleaned_data #리턴값을 꼭 이걸로 해주어야함


class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일', error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'})
    password = forms.CharField(label='비밀번호', min_length=6, max_length=20, widget=forms.PasswordInput)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['introduction', 'profile_image', 'nickname', 'job']

        #한글로 lable 변경하기기
       labels = {
            'introduction': '자기소개',
            'profile_image': '프로필 사진',
            'nickname': '닉네임',
            'job': '역할'
        }