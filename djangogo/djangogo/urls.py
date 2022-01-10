"""djangogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from votes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/', views.user_info),
    path('user/<int:id>', views.user_info_by_id)
    ]
    # path('polls/',views.view_all_polls),
    # path('polls/creat/', views.creat_polls),
    # path('polls/<int:id>/', views.view_poll_by_id),
    # path('polls/<int:id>/vote'), views.vote_poll),

    # ''' 그냥 예시
    # path('admin/', admin.site.urls),
    # path('index/', views.index), ##추가 : index라는 명령어가 들어왔을때 views.index에 접근하겠다
    # path('user/', views.user_info),
    # path('user/<int:id>', views.user_info_by_id) #숫자형식으로 id를 받음, <str:email>로 쓰면 문자형식의 이메일을 받겠다
    # '''

