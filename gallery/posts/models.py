from django.db import models
from django.contrib.auth.models import User

# 작가 모델
class Artist(models.Model):
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]

    STATUS_CHOICES = [
        ('P', '대기중'),  # Pending
        ('A', '승인됨'),  # Approved
        ('R', '거부됨'),  # Rejected
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 사용자와 1:1 관계
    name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='artist_images/', blank=True, null=True)  # 작가 프로필 이미지
    contact = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')  # 작가 상태

    def __str__(self):
        return self.name

# 작품 모델
class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # 작가와 1:N 관계
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hoosu = models.PositiveIntegerField()  # 호수 (1 이상 500 이하의 숫자)
    created_at = models.DateTimeField(auto_now_add=True)
    artwork_image = models.ImageField(upload_to='artwork_images/', blank=True, null=True)  # 작품 이미지

    def __str__(self):
        return self.title

# 전시 모델
class Exhibition(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # 작가와 1:N 관계
    title = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    artworks = models.ManyToManyField(Artwork)  # 다대다 관계 (전시에 포함된 작품들)

    def __str__(self):
        return self.title

# 관리자 모델 (추가적인 사용자 모델이 필요한 경우)
class CustomUser(User):
    # 사용자에 대한 추가 필드를 정의할 수 있습니다.
    pass
