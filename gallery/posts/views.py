# posts/views.py

from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ArtistRegistrationForm
import logging
import re
from django.db.models import Q
import csv
from django.http import HttpResponse
from .models import Artist, Artwork
from .forms import ArtworkForm, ExhibitionForm

class ApiOverview(APIView):
    def get(self, request):
        return Response({"message": "API Overview"}, status=status.HTTP_200_OK)

# 또는 간단한 함수형 뷰로 만들 수도 있습니다.
def api_overview(request):
    return JsonResponse({"message": "API Overview"})

# 메인 페이지 / 작품 조회
def home(request):
    artworks = Artwork.objects.all().order_by('-id')
    return render(request, 'posts/index.html', {'artworks': artworks})

def artwork_list(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter_type', '')
    min_value = request.GET.get('min_value', '')
    max_value = request.GET.get('max_value', '')

    artworks = Artwork.objects.all()

    # 제목 검색
    if query:
        artworks = artworks.filter(title__icontains=query)
    
    # 가격 또는 호수 범위 필터링
    if filter_type and min_value and max_value:
        if filter_type == 'price':
            artworks = artworks.filter(price__gte=min_value, price__lte=max_value)
        elif filter_type == 'hoosu':
            artworks = artworks.filter(hoosu__gte=min_value, hoosu__lte=max_value)

    return render(request, 'posts/index.html', {'artworks': artworks})

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
                messages.success(request, '로그인에 성공했습니다!')
                return redirect('home')
            else:
                messages.error(request, '유효하지 않은 로그인 정보입니다.')
        else:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.') 
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

# 로그아웃
def logout_view(request):
    logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return redirect('home')

# 회원가입
logger = logging.getLogger(__name__)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 성공적으로 완료되었습니다!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'posts/signup.html', {'form': form})

# 작가
def artist_list(request):
    query = request.GET.get('q', '')  # 검색어를 GET 요청에서 가져옴
    search_gender = request.GET.get('gender', '')  # 성별 필터링 추가
    search_birth_date = request.GET.get('birth_date', '')  # 생년월일 필터링 추가

    # 기본적으로 상태가 'A'(승인된) 작가만 필터링
    artists = Artist.objects.filter(status='A').order_by('-id')

    # 검색어가 있는 경우 필터링
    if query:
        artists = artists.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) |
            Q(contact__icontains=query)
        )

    # 성별이 선택된 경우 필터링
    if search_gender:
        artists = artists.filter(gender=search_gender)

    # 생년월일이 선택된 경우 필터링
    if search_birth_date:
        # 날짜 형식인지 확인
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'  # 형식을 YYYY-MM-DD로 변경
        if re.match(date_pattern, search_birth_date):
            artists = artists.filter(birth_date=search_birth_date)

    return render(request, 'posts/artist_list.html', {'artists': artists})

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
            messages.error(request, '이미 등록된 이메일입니다. 다른 이메일을 사용해주세요.')
            return redirect(request.META.get('HTTP_REFERER', 'register_artist'))

        try:
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

            messages.success(request, '작가 등록이 성공적으로 완료되었습니다.')
            return redirect('home')  # 성공적으로 등록 후 리디렉션

        except IntegrityError:
            messages.error(request, '데이터베이스 오류가 발생했습니다. 다시 시도해주세요.')
            return redirect('register_artist')

    return render(request, 'posts/register_artist.html')

# 어드민 페이지
def artist_registration_list(request):
    query = request.GET.get('q', '')
    search_gender = request.GET.get('gender', '')
    search_birth_date = request.GET.get('birth_date', '')

    artists = Artist.objects.all()

    # 이름, 이메일, 연락처, 성별, 생년월일로 검색
    if query:
        artists = artists.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) |
            Q(contact__icontains=query)
        )
    if search_gender:
        artists = artists.filter(gender=search_gender)
    if search_birth_date:
        artists = artists.filter(birth_date=search_birth_date)

    artists = artists.order_by('-id')

    if request.method == 'POST':
        selected_artists = request.POST.getlist('selected_artists')
        action = request.POST.get('action')
        if action == 'approve':
            messages.success(request, '승인되었습니다.')
            Artist.objects.filter(id__in=selected_artists, status='P').update(status='A')
        elif action == 'reject':
            messages.success(request, '거부되었습니다.')
            Artist.objects.filter(id__in=selected_artists, status='P').update(status='R')
        return redirect('artist_registration_list')

    return render(request, 'posts/artist_registration_list.html', {'artists': artists})

# csv 다운로드
def download_csv(request):
    query = request.GET.get('q', '')
    search_gender = request.GET.get('gender', '')
    search_birth_date = request.GET.get('birth_date', '')

    artists = Artist.objects.all()

    if query:
        artists = artists.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) |
            Q(contact__icontains=query)
        )
    if search_gender:
        artists = artists.filter(gender=search_gender)
    if search_birth_date:
        artists = artists.filter(birth_date=search_birth_date)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="artist_registration.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['이름', '성별', '이메일', '연락처', '상태', '생년월일'])

    for artist in artists:
        writer.writerow([artist.name, artist.get_gender_display(), artist.email, artist.contact, artist.get_status_display(), artist.birth_date])
    
    return response

# 작품 등록 페이지
@login_required(login_url='login')
def register_artwork(request):
    if request.method == 'POST':
        # 가격의 콤마 제거
        request.POST = request.POST.copy()
        if 'price' in request.POST:
            request.POST['price'] = request.POST['price'].replace(',', '')

        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user.artist  # 현재 로그인한 사용자의 아티스트 정보
            artwork.save()
            messages.success(request, '작품이 성공적으로 등록되었습니다.')
            return redirect('home')  # URL name 수정
        else:
            messages.error(request, '입력값이 올바르지 않습니다. 다시 확인해주세요.')
    else:
        form = ArtworkForm()
    
    return render(request, 'posts/register_artwork.html', {'form': form})


# 전시 등록 페이지
@login_required
def register_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            # 현재 로그인된 유저의 아티스트 가져오기
            artist = Artist.objects.get(user=request.user)
            exhibition.artist = artist
            exhibition.save()
            
            # 선택된 작품만 저장
            artworks = form.cleaned_data.get('artworks')
            exhibition.artworks.set(artworks)  # 선택된 작품 저장

            messages.success(request, '전시가 성공적으로 등록되었습니다.')
            return redirect('home')
    else:
        form = ExhibitionForm()
    
    return render(request, 'posts/register_exhibition.html', {'form': form})

# 작품 통계 페이지
def artist_statistics(request):
    # 모든 작가 목록을 가져옴
    artists = Artist.objects.all()

    # 통계 데이터를 담을 리스트
    artist_stats = []

    for artist in artists:
        # 해당 작가의 작품 목록을 가져옴
        artworks = Artwork.objects.filter(artist=artist)

        if artworks.exists():
            # 100호 이하의 작품 개수
            artwork_count_below_100 = artworks.filter(hoosu__lte=100).count()

            # 모든 작품의 평균 가격
            average_price = artworks.aggregate(Avg('price'))['price__avg']

            # 가장 비싼 작품
            most_expensive_artwork = artworks.order_by('-price').first()

            # 가장 저렴한 작품
            least_expensive_artwork = artworks.order_by('price').first()

            # 해당 작가의 통계 데이터를 리스트에 추가
            artist_stats.append({
                'artist': artist,
                'artwork_count_below_100': artwork_count_below_100,
                'average_price': average_price if average_price else 0,
                'most_expensive_artwork': most_expensive_artwork,
                'least_expensive_artwork': least_expensive_artwork,
            })
        else:
            artist_stats.append({
                'artist': artist,
                'artwork_count_below_100': 0,
                'average_price': 0,
                'most_expensive_artwork': None,
                'least_expensive_artwork': None,
            })

    return render(request, 'posts/artist_statistics.html', {'artist_stats': artist_stats})
