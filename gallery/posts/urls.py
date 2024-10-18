# posts/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('api/', views.api_overview, name='api-overview'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('artists/', views.artist_list, name='artist_list'),
    path('register_artist/', views.register_artist, name='register_artist'),
    path('artworks/', views.artwork_list, name='artwork_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)