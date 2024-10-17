# posts/urls.py

from django.urls import path
from .views import YourAPIView  # 여기에 실제 API 뷰를 임포트

urlpatterns = [
    path('', YourAPIView.as_view(), name='your_api_view'),
    # 추가적인 API 경로가 필요하면 여기에 추가
]
