from django.db import models
from django.contrib.auth.models import User


# 질문 Question 클래스 생성: subject, content, create_date
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 글자 수 제한
    content = models.TextField()  # 글자 수 제한이 없는 경우
    create_date = models.DateTimeField()  # 날짜 + 시간

    # author필드 추가: 글쓴이
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')

    # 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)
    # null=True: 데이터베이스에서 null 허용, blank=True 등록할 때, validation시 빈칸을 허용하겠다는 것
    # form.is_valid() 입력값 겁증 시 값이 없어도 된다.

    # 추천인
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # on_delete=models.CASCADE: 답변에 연관된 질문이 삭제되면 답변도 모두 삭제하세요.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()  # 글자수 제한이 없는
    create_date = models.DateTimeField()  # 날짜 + 시간

    # author필드 추가: 글쓴이
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')

    # 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)

    # 추천인
    voter = models.ManyToManyField(User, related_name='voter_answer')
    # 입력필드에 null 허용하기
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.IntegerField()
    modify_date = models.DateTimeField(null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
