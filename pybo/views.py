from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    questionList = Question.objects.order_by('-createDate')
    context = {"questionList": questionList}
    return render(request, "pybo/question_list.html", context)
    
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


def answerCreate(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    question.answer_set.create(content=request.POST.get('answerContent'), createDate=timezone.now())
    return redirect('pybo:detail', questionId = question.id)

 