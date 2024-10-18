from django.contrib import admin
from .models import Artist, Artwork, Exhibition, CustomUser

# 작가 모델을 관리자에 등록
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birth_date', 'email', 'contact')
    search_fields = ('name', 'email')
    list_filter = ('gender',)

# 작품 모델을 관리자에 등록
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'hoosu', 'created_at')
    search_fields = ('title',)
    list_filter = ('artist',)

# 전시 모델을 관리자에 등록
@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('artist',)

# 커스텀 사용자 모델을 관리자에 등록
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
