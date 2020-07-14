from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
# from django.http import HttpResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    # page = request.GET.get('page', '1') 은 다음처럼 GET방식으로 요청한 URL에서 page의 값을 가져올때 사용한다. http://localhost:8000/pybo/?page=1 
    # 만약 http://localhost:8000/pybo/ 처럼 page값이 없을 경우에는 디폴트로 1이라는 값을 설정한다.
    questionList = Question.objects.order_by('-createDate')
    paginator = Paginator(questionList, 10)
    pageObj = paginator.get_page(page)
    context = {'questionList': pageObj}
    return render(request, 'pybo/question_list.html', context)
    # A context is a variable name -> variable value mapping that is passed to a template. Context processors let you specify a number of variables that get set in each context automatically – without you having to specify the variables in each render() call.

def detail(request, questionId):
    # question = Question.objects.get(id=questionId)
    question = get_object_or_404(Question, pk=questionId)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

""" 제네릭 뷰(Generic Views) 
class IndexView(generic.ListView):
    def get_queryset(self):
        return Question.objects.order_by("-createDate")

class DetailView(generic.DetailView):
    model = Question 
    
IndexView는 템플릿 명이 명시적으로 지정되지 않은 경우에는 자동으로 모델명_list.html을 템플릿명으로 사용하게 된다. 마찬가지로 DetailView는 모델명_detail.html을 템플릿명으로 사용한다.    """

@login_required(login_url="common:login")
def answerCreate(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.createDate = timezone.now()
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("pybo:detail", questionId=question.id)
        else:
            return render(request, "pybo/question_detail.html", {'question':question, 'form':form})    
    else:
        form = AnswerForm()
        context = {'question':question, 'form':form}
        return render(request, "pybo/question_detail.html", context)

@login_required(login_url="common:login")
def questionCreate(request):
    if request.method =="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.createDate=timezone.now()
            question.save()
            return redirect("pybo:index")
        else:
            return render(request, "pybo/question_form.html", {'form':form})
    else:
        form = QuestionForm()
        return render(request, "pybo/question_form.html", {'form':form})
            

            
    