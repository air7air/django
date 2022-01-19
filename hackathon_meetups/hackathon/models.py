from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    ) #내 회원정보가 삭제가 되면 참가신청 정보도 삭제가 되어야 하니까 CASECADE
    introduction = models.TextField(null=False, max_length=300) #null=False빈칸금지 #캐릭터필드:한줄짜리 입력, 텍스트필드:여러줄 입력 가능
    profile_image = models.ImageField(upload_to='uploads/%Y/%m/%d/') #파일 이미지를 업로드 할때 사용, upload_to:프로젝트 내에 파일이 저장되는 경로
    nickname = models.CharField(null=False, max_length=10)
    job = models.CharField(null=False, max_length=100)
