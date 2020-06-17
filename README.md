## Wecode 7기 기업협업 Brandi Admin Clone Repository
### 프로젝트 소개
모바일 패션 커머스 플랫폼 [브랜디 어드민](http://admin.brandi.co.kr/login) clone project

### 개발 인원 및 기간
- 기간 : 2020.05.25 - 2020.06.18 (약 4주)
- 개발 인원 : 프론트엔드 [one-iron](https://github.com/one-iron) 백엔드 [yeeunlee](https://github.com/yenilee), [sungjun-jin](https://github.com/sungjun-jin)

### 기술
- Python, Flask
- Flask CORS headers
- JSON Schema
- Bcrypt
- JSON Web Token
- MySQL
- AWS EC2, RDS

### 기능
- 셀러 / 마스터 회원가입, 로그인
- 셀러, 상품 validation check
- Password encryption with Bcypt
- JSON Web Token을 활용한 access token 발행
- 셀러 등록 / 수정
- 셀러 리스트
- 상품 등록 / 수정
- 상품 리스트
- Project deployment with AWS EC2 
- AWS RDS에 DB 세팅 및 EC2 서버 연결

### requirements.txt
```sh
$ pip install -r requirements.txt
```
### API Documentation (with POSTMAN)
Endpoint Documentation [URL](https://documenter.getpostman.com/view/10871584/Szzj8HuL?version=latest#aec8e97f-6b27-45a4-9b7c-91e184832f4e)

### ERD (with AQUERY Tool)
AQUERY Tool [URL](https://aquerytool.com:443/aquerymain/index/?rurl=fc0d6178-7128-43ae-b371-04042d84c0d6)
password : xdd757
![ERD](https://images.velog.io/images/sungjun-jin/post/e8b064a6-4f58-401f-b0ab-338ae2371f67/image.png)
