# REST API 실습 서버

학과 REST API 실습을 위한 테스트 서버입니다. Swagger UI를 통해 각 API의 사용법을 확인할 수 있습니다.

## 실행 방법

```bash
pip install -r requirements.txt
python run.py
```

서버가 실행되면 브라우저에서 Swagger UI에 접속하여 API를 테스트할 수 있습니다.

- **Swagger UI**: http://210.101.236.166/docs

## 서버 배포 (Linux)

```bash
cd /root
git clone https://github.com/gsc-lab/rest_api.git
cd rest_api
pip install -r requirements.txt
```

### 데몬 등록

`rest-api.service` 파일이 프로젝트에 포함되어 있으며, `/root/rest_api` 경로 기준으로 설정되어 있습니다.

```bash
sudo cp rest-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rest-api    # 부팅 시 자동 시작
sudo systemctl start rest-api     # 서비스 시작
```

### 서비스 관리

```bash
sudo systemctl status rest-api    # 상태 확인
sudo systemctl restart rest-api   # 재시작
sudo journalctl -u rest-api -f    # 로그 확인
```

### 코드 업데이트 반영

```bash
cd /root/rest_api
git pull
sudo systemctl restart rest-api
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
