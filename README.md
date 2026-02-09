# REST API 실습 서버

학과 REST API 실습을 위한 테스트 서버입니다. Swagger UI를 통해 각 API의 사용법을 확인할 수 있습니다.

## 실행 방법

### Docker (권장)

```bash
docker compose up -d
```

http://localhost/docs 에서 Swagger UI에 접속할 수 있습니다.

### 로컬 실행

```bash
pip install -r requirements.txt
python run.py
```

http://localhost:5001/docs 에서 Swagger UI에 접속할 수 있습니다.

## 서버 배포

```bash
git clone https://github.com/gsc-lab/rest_api.git
cd rest_api
docker compose up -d
```

### 코드 업데이트 반영

```bash
cd rest_api
git pull
docker compose up -d --build
```

## API 시나리오

### Todo

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/todo/{user_id}/todos` | 할 일 목록 조회 |
| POST | `/api/todo/{user_id}/todos` | 할 일 추가 |
| PATCH | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 수정 |
| DELETE | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 삭제 |
| GET | `/api/todo/users` | 사용자 목록 조회 |
