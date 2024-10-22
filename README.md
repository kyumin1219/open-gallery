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
python3 manage.py migrate
```

### 4. 서버 실행

```bash
python3 manage.py runserver
```
