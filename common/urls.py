from django.urls import path

from django.contrib.auth import views as authViews

from . import views 

app_name = 'common'
urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name = 'common/login.html'),name="login"),
    path('logout/', authViews.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
]

# You just can't use class-based views like you could in normal function-based views. In Class-based views, you have to call as_view() function so as to return a callable view that takes a request and returns a response. Its the main entry-point in request-response cycle in case of generic views.

# 로그인/로그아웃과 달리 계정생성은 LoginView, LogoutView와 같은 뷰가 제공되지 않기 때문에 계정생성을 위한 뷰 함수를 직접 만들어야 한다.