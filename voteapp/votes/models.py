from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False) #레코드가 추가될때 알아서 입력된 시간이 저장됨

    #이거 안쓰면 문자열로 안나옴
    # __str__:클래스를 표현하는 문자열을 정의할 수 있는 메소드(모델의 의미를 표현하고 싶을 때도 오버라이드 해서 사용가능)
    def __str__(self):
        return self.title


class Option(models.Model):
    name = models.CharField(max_length=20, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False) #첫번째:종속 데이터, on_delate 연결된 것 모두 삭제되도록


    # __str__:클래스를 표현하는 문자열을 정의할 수 있는 메소드(모델의 의미를 표현하고 싶을 때도 오버라이드 해서 사용가능)
    def __str__(self):
        return self.name


class Vote(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
