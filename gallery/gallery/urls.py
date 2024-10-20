"""
URL configuration for gallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import posts.views


urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 URL
    path('', posts.views.home, name='home'),  # 메인 페이지
    path('signup/', posts.views.signup, name='signup'),  # 회원가입 페이지
    path('api/signup/', posts.views.signup, name='signup'),  # API 회원가입 엔드포인트
    path('login/', posts.views.login_view, name='login'),  # 로그인 페이지
    path('logout/', posts.views.logout_view, name='logout'),  # 로그아웃 페이지
    path('register_artist/', posts.views.register_artist, name='register_artist'),  # 작가 신청 페이지
    path('artist_registration_list/', posts.views.artist_registration_list, name='artist_registration_list'),  # 작가 신청 내역 조회 페이지
    path('', include('posts.urls')),
]