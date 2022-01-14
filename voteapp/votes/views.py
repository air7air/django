from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PollCreateForm, VoteForm, PollUpdateForm
from .models import Topic, Vote, Option


def view_all_polls(request):
    topics = Topic.objects.all() #all: 모든 데이터 불러와
    context = {
        'topics': topics
    }
    return render(request, 'pages/view_all_polls.html', context) #중요 render:3개의 인자를 받음 1.request, 2.템플릿 경로, 3 딕셔너리 객체


def create_poll(request):
    # 포스트로 접근했을때
    if request.method == 'POST':
        form = PollCreateForm(request.POST)
        if form.is_valid(): #폼에 모두 맞게 정상적으로 돌아간다면(검증했다면)
            title = form.cleaned_data['topic']
            options = form.cleaned_data['options'].split(',') # 선택지를 쉼표 구분으로 전달받을 예정

            # topic 저장
            topic = Topic(title=title)
            topic.save()

            # options 저장
            for item in options:
                Option.objects.create(name=item, topic=topic) # create 함수: 인스턴스 생성하자마자 저장할수 있음(위에 두줄 한줄로 표현 가능)

            return HttpResponseRedirect('/polls/')
    #포스트아닐때
    else:
        form = PollCreateForm()

    context = {
        'create_form': form
    }
    return render(request, 'pages/create_poll.html', context)


def view_poll_by_id(request, id):
    topic = Topic.objects.get(id=id) #get():데이터를 하나 특정해서 가져온다 앞의 / id:속성 뒤 id:변수
    options = Option.objects.filter(topic=topic).all() #get은 하나만 가져와서 대신 filter를 씀
    # filter():특정 조건과 일치하는 레코드 탐색

    # 전체득표수
    total_votes = Vote.objects.filter(topic=topic).count()

    results = {}

    for item in options:
        vote_count = Vote.objects.filter(option=item).count()
        if total_votes > 0: #전체수표수가 0일때 나누기 0을 하면 오류가 나기때문에 1개 이상일때만 계산되도록
            percent = vote_count / total_votes * 100
            result_text = "투표 수: %d, 비율: %.2f" % (vote_count, percent)
        else:
            result_text = "투표 없음"
        # 마지막으로 딕셔너리에 이름을 키로해서 넣어둠
        results[item.name] = result_text

    # 랜더링하기위해
    context = {
        'topic': topic,
        'results': results
    }

    return render(request, 'pages/view_poll_by_id.html', context)


def vote_poll(request, id):
    topic = Topic.objects.get(id=id) #템플릿 변수의 topic을 넘기는것을 잊지말고 넣어주자

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid(): #통과하면
            form.save() #데이터를 db에 바로 저장
            return HttpResponseRedirect('/polls/%d' % id) #상세보기 페이지로 돌아가기
    else:
        form = VoteForm() #데이터가 없는 형태로 랜더링

    form.fields['topic'].initial = topic #initial:폼의 초기값을 지정할 수 있음
    form.fields['option'].queryset = Option.objects.filter(topic=topic).all()

    context = {
        'form': form,
        'topic': topic
    }

    return render(request, 'pages/vote_poll.html', context)

#수정기능
def update_poll(request, id):
    topic = Topic.objects.get(id=id)

    if request.method == 'POST':
        form = PollUpdateForm(request.POST, instance=topic) #새로운 데이터를 생성하는것이 아니라 topic에 POST로 받은 데이터를 집어넣어줌(결합시켜줌)
        if form.is_valid():
            form.save()

            # 기존 옵션 삭제
            Option.objects.filter(topic=topic).delete()

            # 새로운 옵션을 추가
            options_new = form.cleaned_data['options'].split(',')
            for item in options_new:
                Option.objects.create(name=item, topic=topic)

            return HttpResponseRedirect('/polls/%d/' % id)
    else:
        form = PollUpdateForm(instance=topic)

    # 옵션 수정
    options = Option.objects.filter(topic=topic).all() #현재 보고있는 토픽기준으로 뽑아낸다음
    joined = ",".join(item.name for item in options) #그 아이들을 쉼표 기준으로 다 join함
    form.fields['options'].initial = joined

    context = {
        'update_form': form,
        'topic': topic
    }

    return render(request, 'pages/update_poll.html', context)


def delete_poll(request, id):
    topic = Topic.objects.get(id=id)
    topic.delete()

    return HttpResponseRedirect('/polls') #첫페이지로 돌아가기