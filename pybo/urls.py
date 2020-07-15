from django.urls import path

from . import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:questionId>/', views.detail, name="detail"),
    path('answer/create/<int:questionId>/', views.answerCreate, name="answer_create"),
    path("question/create/", views.questionCreate, name="question_create"),
    path("question/modify/<int:question_id>/", views.questionModify, name="question_modify"),
    path('question/delete/<int:questionId>/', views.questionDelete, name="question_delete"),
    path('answer/modify/<int:answerId>/', views.answerModify, name="answer_modify"),
    path('answer/delete/<int:answerId>/', views.answerDelete, name="answer_delete"),
    path('comment/create/question/<int:questionId>/', views.commentCreateQuestion, name="comment_create_question"),
    path('comment/modify/question/<int:commentId>/', views.commentModifyQuestion, name="comment_modify_question"),
    path('comment/delete/question/<int:commentId>/', views.commentDeleteQuestion, name="comment_delete_question"),
    path('comment/create/answer/<int:answerId>/', views.commentCreateAnswer, name='comment_create_answer'),
    path('comment/modify/answer/<int:commentId>/', views.commentModifyAnswer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:commentId>/', views.commentDeleteAnswer, name='comment_delete_answer'),
]

""" 제네릭 뷰(Generic Views) 
app_name = 'pybo'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>', views.DetailView.as_view()),
]    """
