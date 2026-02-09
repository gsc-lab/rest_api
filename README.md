# REST API 실습 서버

학과 REST API 실습을 위한 테스트 서버입니다. Swagger UI를 통해 각 API의 사용법을 확인할 수 있습니다.

- **Swagger UI**: http://210.101.236.166/docs

## 실행 방법

### Docker (권장)

```bash
docker compose up -d
```

### 로컬 실행

```bash
pip install -r requirements.txt
python run.py
```

## 서버 주소 변경

기본 서버 주소는 `210.101.236.166:80`입니다. 변경이 필요한 경우 아래 파일을 수정하세요.

| 파일 | 설명 |
|------|------|
| `run.py` | 로컬 실행 시 `HOST`, `PORT` 기본값 |
| `docker-compose.yml` | Docker 실행 시 포트 매핑 (`ports`) |

환경변수로도 오버라이드할 수 있습니다.

```bash
HOST=0.0.0.0 PORT=5001 python run.py
```

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
