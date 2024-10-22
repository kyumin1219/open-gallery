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

### 4. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 서버 실행

```bash
python3 manage.py runserver
```

## 배포된 사이트
이 프로젝트는 AWS EC2를 사용해 배포되었습니다. 다음 주소에서 사이트를 확인할 수 있습니다:

사이트 주소: http://3.37.212.42:8000/home/

## 주요 URL
고객 페이지: http://localhost:8000/
관리자 페이지: http://localhost:8000/admin/
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

## 향후 작업

- **검색 및 필터 기능**: 사용자가 작가나 작품을 쉽게 검색할 수 있는 기능 추가 예정.
- **RESTful API 개발**: Django REST Framework를 활용하여 API 엔드포인트 추가 예정.
- **작품 이미지 업로드 최적화**: 대용량 이미지 파일 업로드 시 처리 성능 개선 작업 예정.
