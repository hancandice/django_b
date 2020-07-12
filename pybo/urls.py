from django.urls import path

from . import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:questionId>/', views.detail, name="detail"),
    path('answer/create/<int:questionId>/', views.answerCreate, name="answer_create"),
    path("question/create/", views.questionCreate, name="question_create"),
]

""" 제네릭 뷰(Generic Views) 
app_name = 'pybo'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>', views.DetailView.as_view()),
]    """
