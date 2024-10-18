# posts/views.py

from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ArtistRegistrationForm
import logging
import re
from .models import Artist, Artwork

class ApiOverview(APIView):
    def get(self, request):
        return Response({"message": "API Overview"}, status=status.HTTP_200_OK)

# 또는 간단한 함수형 뷰로 만들 수도 있습니다.
def api_overview(request):
    return JsonResponse({"message": "API Overview"})

# 메인 페이지
def home(request):
    return render(request, "posts/index.html")

# 로그인
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('home')

# 회원가입
logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # create_user를 호출하지 않고 form.save()를 통해 User를 생성
            login(request, user)  # 자동 로그인
            messages.success(request, '회원가입이 성공적으로 완료되었습니다!')  # 성공 메시지 추가
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'posts/signup.html', {'form': form})

# 작가
def artist_list(request):
    artists = Artist.objects.all().order_by('-id')
    return render(request, 'posts/artist_list.html', {'artists': artists})

# 작품
def artwork_list(request):
    artworks = Artwork.objects.all().order_by('-id')
    return render(request, 'posts/artwork_list.html', {'artworks': artworks})

# 작가 신청
@login_required(login_url='login')  # 로그인 페이지 URL을 지정
def register_artist(request):
    if Artist.objects.filter(user=request.user).exists():
        messages.error(request, '이미 아티스트로 등록된 사용자입니다.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))  # 이전 페이지로 리디렉션

    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        # 이메일 중복 확인
        if Artist.objects.filter(email=email).exists():
            messages.error(request, '이미 사용 중인 이메일입니다.')
            return render(request, 'posts/register_artist.html')  # 오류 메시지를 표시한 후 현재 페이지 유지

        # Artist 모델에 저장
        artist = Artist.objects.create(
            profile_image=profile_image,
            name=name,
            gender=gender,
            birth_date=birth_date,
            email=email,
            contact=contact,
            user=request.user,
            status='P'  # 상태를 '대기중'으로 설정
        )

        messages.success(request, '작가 등록이 성공적으로 완료되었습니다.')  # 성공 메시지 추가
        return redirect('home')  # 성공적으로 등록 후 리디렉션
     
    return render(request, 'posts/register_artist.html')