# ArtTech Backoffice Platform

미술품 투자 서비스를 운영하기 위한 Django 기반 백오피스 시스템입니다.  
관리자가 미술품, 투자 정보, 사용자 데이터를 관리할 수 있도록 설계되었습니다.

## Tech Stack

### Backend
- Python 3.11
- Django
- Django REST Framework

### Infrastructure
- Docker
- Gunicorn
- Nginx

### Database
- PostgreSQL

### Deployment
- AWS ECS (Fargate)
- AWS ECR

### CI/CD
- CircleCI

### API Documentation
- Swagger (drf-spectacular)

### Collaboration
- Bitbucket
- Jira
- Confluence


## Main Features

### Admin Dashboard
- 서비스 운영을 위한 관리자 대시보드
- 미술품 및 투자 데이터 통계 확인

### Artwork Management
- 미술품 등록 / 수정 / 삭제
- 작품 정보 및 투자 정보 관리

### Investment Management
- 투자 상품 관리
- 투자 현황 조회

### User & Permission Management
- 사용자 계정 관리
- 관리자 권한 기반 접근 제어


## Architecture


## Deployment

Docker 기반으로 애플리케이션을 컨테이너화하고  
AWS ECS(Fargate)를 통해 배포했습니다.

CI/CD는 CircleCI를 통해 자동 빌드 및 테스트가 진행됩니다.