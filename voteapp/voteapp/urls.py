"""voteapp URL Configuration

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
from django.urls import path
from votes import views

#증요 name: template(viwe_all_polls.html)에서 불러와서 쓸수 있도록 해줌
#ex
#<a href="/polls/{{ item.id }}/"> 였던 구문을
#<a href="{% url 'view_poll_by_id' item.id %}">로 변경해서 사용 가능

urlpatterns = [
    path('', views.view_all_polls), #첫페이지를 지정하는 path를 views.view_all_polls로 정하겠다 (공백 넣어서 설정)

    path('polls/', views.view_all_polls, name='view_all_polls'), #모든 주제 목록
    path('polls/create/', views.create_poll, name='create_poll'), #투표 주제 만들기
    path('polls/<int:id>/', views.view_poll_by_id, name='view_poll_by_id'), #투표목록에서 id 결과 확인하는 화면
    path('polls/<int:id>/vote', views.vote_poll, name='vote_poll'), #투표를 하는것
    path('polls/<int:id>/update/', views.update_poll, name='update_poll'), #업데이트 화면
    path('polls/<int:id>/delete/', views.delete_poll, name='delete_poll') #주제 지우는 화면
]

# ''' 그냥 예시
# path('admin/', admin.site.urls),
# path('index/', views.index), ##추가 : index라는 명령어가 들어왔을때 views.index에 접근하겠다
# path('user/', views.user_info),
# path('user/<int:id>', views.user_info_by_id) #숫자형식으로 id를 받음, <str:email>로 쓰면 문자형식의 이메일을 받겠다
# '''