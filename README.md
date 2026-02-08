# REST API 실습 서버

학과 REST API 실습을 위한 테스트 서버입니다. Swagger UI를 통해 각 API의 사용법을 확인할 수 있습니다.

## 실행 방법

```bash
pip install -r requirements.txt
python run.py
```

서버가 실행되면 브라우저에서 Swagger UI에 접속하여 API를 테스트할 수 있습니다.

- **Swagger UI**: http://localhost:5001/docs

## API 시나리오

### Todo

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/todo/{user_id}/todos` | 할 일 목록 조회 |
| POST | `/api/todo/{user_id}/todos` | 할 일 추가 |
| PATCH | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 수정 |
| DELETE | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 삭제 |
| GET | `/api/todo/users` | 사용자 목록 조회 |
