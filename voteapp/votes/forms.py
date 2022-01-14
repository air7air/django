from django import forms
from .models import Vote, Topic


class PollCreateForm(forms.Form):
    topic = forms.CharField(label='투표 주제', min_length='2', max_length='50')
    options = forms.CharField(label='투표 선택 옵션', min_length='2', max_length='300')

#수정기능-vote_poll.html
class PollUpdateForm(forms.ModelForm):
    #옵션 수정
    options = forms.CharField(label='투표 선택 옵션', min_length=2, max_length=300)

    #타이틀 수정
    class Meta:
        model = Topic
        fields = ['title'] #타이틀만 수정가능
        #title을 제목으로 바꾸어 보이겠다
        labels = {
            'title': '제목'
        }


class VoteForm(forms.ModelForm):
    #투표를 할때 내가 선택한것이 나와야되는데 모두 다 나와서 선택한 것이 나오도록 덮여씌워지도록 해줌
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), widget=forms.HiddenInput())
    #queryset:모든 오프젝트를 일단 넣고
    #widget:이 필드를 안보이게 할게
    class Meta:
        model = Vote
        fields = ['topic', 'option']
        labels = {
            'option': '선택지'
        }
