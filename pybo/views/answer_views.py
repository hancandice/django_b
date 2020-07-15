from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
# from django.http import HttpResponse
from ..models import Question, Answer, Comment
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


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

