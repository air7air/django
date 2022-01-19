from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ApplicationForm
from .models import Application
from django.db.models import ObjectDoesNotExist #db에서 데이터가 없을때 예외처리하기 위해 불러오기

#첫번째
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) #1부분
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=email, password=password) #인증하기
            if user: #로그인 성공시 (유저가 있다면)
                auth.login(request, user)
                return HttpResponseRedirect('/') #첫페이지로 보내기
            else: #로그인 실패시 (유저가 없다면)
                messages.warning(request, '계정 혹은 비밀번호를 확인해주세요.') #messages:메세지를 출력할수 있게 해줌
    else:
        form = LoginForm()

    context = {
        'form': form #로그인 실패시 여기로 넘어와 '1부분'의 정보를 그대로 담아서
    }
    return render(request, 'pages/login.html', context) #context :이전에 있는 값을 그대로 담아서 보여줌

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(email, email, password) #create_user써야함
            return HttpResponseRedirect('/') #첫페이지에 돌아가기
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'pages/register.html', context)


def logout(request): #로그아웃을 하면 따로 창이 뜰 필요없이 첫페이지로 돌아가도록 해서 템플릿이 필요 없음
    auth.logout(request)
    return HttpResponseRedirect('/')


def update_application(request):
    if not request.user.is_authenticated: #현재 로그인되어있지 않다면
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid(): #기존 데이터가 있을시
            application = form.save(commit=False) #save할때 아무것도 안써주면 db에 저장함. commit=False를 입력시 db에 저장하지 않고 모델 인스턴스만 리턴됨
            application.user = request.user #'로그인된 유저'라는 객체가 application유저로 들어감(새로운 정보가 업데이트됨)

            try: #objects.get이 하나의 값이 없다면 항상 예외를 발생시키기 때문에 try, except 구문 사용
                original = Application.objects.get(user=request.user) #리퀘스트 유저로 지정해 검색 / objects.get:하나의 값을 조회
                application.id = original.id
            except ObjectDoesNotExist: #만약 검색했을때 검색되지 않을때 예외처리
                pass
            finally:
                application.save()

            return HttpResponseRedirect('/application/update/')
    else: #get으로 요청받았을때
        try:
            original = Application.objects.get(user=request.user) #기존 데이터 불러오기
            form = ApplicationForm(instance=original) #instace에 오리지널 데이터를 넣어서 기존 데이터가 채워지도록
            cancelable = True #취소 플래그 ->update_application.html에서 보여지게 함
        except ObjectDoesNotExist: #없을때
            form = ApplicationForm() #빈폼
            cancelable = False #취소 플래그

    context = {
        'form': form,
        'cancelable': cancelable
    }
    return render(request, 'pages/update_application.html', context)


def view_applications(request): #마지막
    applications = Application.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'pages/view_applications.html', context)


def cancel_application(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    try:
        original = Application.objects.get(user=request.user)
        original.delete()
    except ObjectDoesNotExist:
        pass

    return HttpResponseRedirect('/')