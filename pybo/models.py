from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) # 제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용해야 한다. 
    content = models.TextField()
    # 내용(content)처럼 글자수를 제한할 수 없는 텍스트는 위처럼 TextField를 사용해야 한다.
    createDate = models.DateTimeField()
    # 작성일시처럼 날짜와 시간에 관계된 속성은 DateTimeField를 사용해야 한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modifyDate = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject
    # ※ 모델에 메서드가 추가될 경우에는 makemigrations와 migrate 를 수행할 필요는 없다. migrate가 필요한 경우는 모델의 속성이 변경되었을 때뿐이다.    

class Answer(models.Model):
    # 기존 모델을 속성으로 가져갈 경우 ForeignKey를 이용해야 한다. ForeignKey는 다른 모델과의 연결을 의미한다. on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Question과 Answer는 서로 연결되어 있기 때문에 answer_set을 사용하면 질문과 연결된 답변을 가져올 수 있다. Answer모델에서 ForignKey로 Question을 연결해 주었기 때문에 answer_set이 가능해진 것이다.
    content = models.TextField()
    createDate = models.DateTimeField()
    modifyDate = models.DateTimeField(null=True, blank=True)

    # null=True의 의미는 modify_date를 데이터베이스에 저장할때 null이 허용된다는 의미이다. blank=True의 의미는 입력 폼 데이터 체크시(form.is_valid()) 값이 없어도 오류를 내지 않는다는 의미이다. 즉, null=True, blank=True을 사용하면 어떤 조건으로든 값을 비워둘수 있음을 의미한다. 수정일시는 수정이 발생할 경우에만 생성되는 데이터이므로 null=True, blank=True 속성을 지정하였다.

# 이제 작성한 모델을 이용하여 테이블들을 생성해 보자. 테이블 생성을 위해 가장 먼저 해야 할 일은 pybo앱을 config/settings.py 파일의 INSTALLED_APPS 항목에 추가하는 일이다.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createDate = models.DateTimeField()
    modifyDate = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)



# 장고의 기능을 개발하는 패턴

# 템플릿에 추가 기능을 위한 링크(버튼등)추가
# urls.py에 링크에 해당되는 URL 매핑을 작성
# forms.py에 폼 작성 (폼이 필요없는 경우에는 생략)
# views.py에 URL매핑에 의해 실행되는 함수 작성
# 함수에서 사용하는 템플릿 작성    

