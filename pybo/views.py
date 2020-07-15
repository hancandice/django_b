from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
# from django.http import HttpResponse
from .models import Question, Answer, Comment
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            
@login_required(login_url="common:login")
def questionModify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'Not authorized to modify')
        return redirect('pybo:detail', questionId=question_id)    
    else:
        if request.method == "GET":
            form = QuestionForm(instance=question)
            context = {'form':form}
            return render(request, 'pybo/question_form.html' , context)    
        else:
            form = QuestionForm(request.POST, instance=question)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.modifyDate = timezone.now()
                question.save()
                return redirect('pybo:detail', questionId=question.id)
            else:
                return render(request, 'pybo/question_form.html', {'form':form})    



@login_required(login_url='common:login')                
def questionDelete(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.user != question.author:
        messages.error(request, 'Not authorized to delete')
        return redirect('pybo:detail', questionId=question.id)
    question.delete()
    return redirect('pybo:index')


@login_required(login_url='common:login')
def answerModify(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    if request.user != answer.author:
        messages.error(request, 'Not authorized to modify')
        return redirect('pybo:detail', questionId=answer.question.id)
    else:
        if request.method == "GET":
            form = AnswerForm(instance=answer)
            context = {'answer':answer, 'form':form}
            return render(request, 'pybo/answer_form.html', context)
        else:
            form = AnswerForm(request.POST,instance=answer)    
            if form.is_valid():
                answer = form.save(commit=False)
                answer.author = request.user
                answer.modifyDate = timezone.now()
                answer.save()
                return redirect('pybo:detail', questionId = answer.question.id)
            else:
                context = {'answer':answer, 'form':form}
                return render(request, 'pybo/answer_form.html', context)   

@login_required(login_url='common:login')
def answerDelete(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    if request.user != answer.author:
        messages.error(request, 'Not authorized to delete')
    else:
        answer.delete()
    return redirect('pybo:detail', questionId=answer.question.id)

@login_required(login_url='common:login')
def commentCreateQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.method == "GET":
        form = CommentForm()
        context = {'form':form}
        return render(request, 'pybo/comment_form.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.createDate = timezone.now()
            comment.question = question
            comment.save()
            return redirect('pybo:detail', questionId=question.id)
        else:
            return render(request, 'pybo/comment_form.html', {'form':form})

@login_required(login_url='common:login')
def commentModifyQuestion(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, "Not authorized to modify")
        return redirect('pybo:detail', questionId=comment.question.id)
    else:
        if request.method == "GET":
            form = CommentForm(instance=comment)
            context = {'form':form}
            return render(request, 'pybo/comment_form.html', context)
        else:
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.modifyDate = timezone.now()
                comment.save()
                return redirect('pybo:detail', questionId=comment.question.id)
            else:
                context = {'form':form}
                return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def commentDeleteQuestion(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, 'Not authorized to delete')
        return redirect('pybo:detail', questionId=comment.question.id)
    else:
        comment.delete()
        return redirect('pybo:detail', questionId=comment.question.id)



@login_required(login_url='common:login')
def commentCreateAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    if request.method == "GET":
        form = CommentForm()
        context = {'form':form}
        return render(request, 'pybo/comment_form.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.createDate = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('pybo:detail', questionId=answer.question.id)
        else:
            return render(request, 'pybo/comment_form.html', {'form':form})

@login_required(login_url='common:login')
def commentModifyAnswer(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, "Not authorized to modify")
        return redirect('pybo:detail', questionId=comment.answer.question.id)
    else:
        if request.method == "GET":
            form = CommentForm(instance=comment)
            context = {'form':form}
            return render(request, 'pybo/comment_form.html', context)
        else:
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.modifyDate = timezone.now()
                comment.save()
                return redirect('pybo:detail', questionId=comment.answer.question.id)
            else:
                context = {'form':form}
                return render(request, 'pybo/comment_form.html', context)

@login_required(login_url='common:login')
def commentDeleteAnswer(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, 'Not authorized to delete')
        return redirect('pybo:detail', questionId=comment.answer.question.id)
    else:
        comment.delete()
        return redirect('pybo:detail', questionId=comment.answer.question.id)