# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Server

```bash
pip install -r requirements.txt
python run.py
```

Runs on `0.0.0.0:5001` with debug mode. Swagger UI available at `/docs`.

## Architecture

학과 REST API 실습용 테스트 서버. Flask + Flask-RESTX 기반이며 Swagger UI로 학생들에게 API 사용법을 제공한다.

```
app/
├── __init__.py        # App factory (create_app)
└── apis/
    ├── __init__.py    # Api 객체 생성, 네임스페이스 등록
    └── todo.py        # Todo API 시나리오
```

- **App Factory 패턴**: `app/__init__.py`의 `create_app()`에서 Flask 앱 생성, CORS, Api 초기화
- **Api 등록**: `app/apis/__init__.py`에서 Flask-RESTX `Api` 객체를 만들고 네임스페이스를 등록
- **시나리오별 모듈**: 각 API 시나리오는 `app/apis/` 아래 별도 파일로 존재하며 자체 `Namespace`를 갖는다
- **Storage**: 인메모리 dict. 서버 재시작 시 데이터 소멸
- **ID 생성**: Unix timestamp 밀리초 (`int(time.time() * 1000)`)

### 새 API 시나리오 추가 방법

1. `app/apis/`에 새 파일 생성 (예: `board.py`)
2. `Namespace` 생성, Swagger 모델 정의, `Resource` 클래스 작성
3. `app/apis/__init__.py`에서 import 후 `api.add_namespace(ns, path="/api/board")` 등록

### Todo API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/todo/{user_id}/todos` | 사용자의 할 일 목록 조회 |
| POST | `/api/todo/{user_id}/todos` | 할 일 추가 (`text` 필수) |
| PATCH | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 수정 (`text`, `completed`) |
| DELETE | `/api/todo/{user_id}/todos/{todo_id}` | 할 일 삭제 |
| GET | `/api/todo/users` | 전체 사용자 및 할 일 개수 조회 |

### Code Conventions

- Resource 클래스가 라우트 그룹에 대응
- Swagger 모델(`ns.model`)로 request/response 스키마 정의
- 주석과 docstring은 한국어
- 교육용 프로젝트 — 인메모리 저장소, 인증 없음
