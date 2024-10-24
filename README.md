# Open Gallery

**Open Gallery**는 작가와 작품을 등록하고, 전시 정보를 관리할 수 있는 시스템입니다. 이 프로젝트는 고객 페이지, 관리자 페이지, 작가 페이지를 포함하여 전시 등록 및 조회 기능을 제공합니다.

## 주요 기능

- 작가 등록 및 관리
- 작품 등록 및 조회
- 전시 등록 (제목, 시작일, 종료일, 작품 목록 입력 가능)
- 관리자 페이지에서 전시 정보 관리
- 사용자의 로그인 및 권한 시스템 (고객, 관리자, 작가)

## 설치 및 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/your-username/open-gallery.git
cd open-gallery
```

### 2. 가상환경 설정

```bash
# 가상 환경 생성 (Python3 기준)
python3 -m venv venv

# 가상 환경 활성화 (Mac/Linux)
source venv/bin/activate

# 가상 환경 활성화 (Windows)
venv\Scripts\activate
```

### 3. 필수 패키지 설치

```bash
# requirements.txt 파일에 명시된 프로젝트 패키지들을 설치합니다.
pip install -r requirements.txt
```

### 4. 패키지 추가 설치

```bash
# 하나씩 복사해서 requirements.txt 파일에 추가합니다.
djangorestframework>=3.12,<4.0
Pillow>=8.0
```

## 5. 어드민 계정 생성
```bash
python3 manage.py createsuperuser
# 아이디, 이메일, 비밀번호을 입력 후 localhost:<포트>/admin 접속합니다.
# 생성한 어드민 계정의 아이디 비밀번호로 로그인하여 DB의 값들을 확인할 수 있습니다.
```

### 6. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. 서버 실행

```bash
python3 manage.py runserver
```


## 배포된 사이트
이 프로젝트는 AWS EC2를 사용해 배포되었습니다. 다음 주소에서 사이트를 확인할 수 있습니다:

사이트 주소: http://3.37.212.42:8000/home/

## 주요 URL
고객 페이지: http://3.37.212.42:8000/home/

관리자 페이지: http://3.37.212.42:8000/admin/

작가 페이지: 작가로 로그인 시 이용 가능

## 기술 스택

- **Django** - Python 기반 웹 프레임워크
- **Django REST Framework** - API 개발
- **SQLite** - 데이터베이스
- **Pillow** - 이미지 처리 라이브러리
- **AWS EC2** - 배포 인프라

## 문제 해결 과정

1. **이미지 업로드 문제**
   - 문제: 이미지 파일 업로드 시 용량이 큰 파일로 인해 서버 응답 속도가 느려지는 문제 발생.
   - 해결: `Pillow` 라이브러리를 사용하여 업로드 전 이미지 리사이징 및 최적화를 적용.

## 추후 계획

- **검색 및 필터 기능**: 사용자가 작가나 작품을 쉽게 검색할 수 있는 기능 추가 예정.
- **RESTful API 개발**: Django REST Framework를 활용하여 API 엔드포인트 추가 예정.
- **작품 이미지 업로드 최적화**: 대용량 이미지 파일 업로드 시 처리 성능 개선 작업 예정.

## 느낀점

- 이번 프로젝트를 통해 Django로 사용자 인증, 데이터 관리 등 웹 애플리케이션 설계 및 구현 능력을 발전시킬 수 있었습니다. 또한, AWS EC2 배포 과정을 경험하며 서버 설정과 유지보수에 대한 실무적 이해도 높였습니다. 특히, 이미지 업로드 최적화 문제를 해결하면서 성능 최적화의 중요성을 깨달았고, 이를 통해 사용자 경험을 개선하는 방법을 배울 수 있었습니다. 앞으로 검색 및 필터 기능, RESTful API 개발 등을 통해 프로젝트를 확장할 계획입니다.
  
