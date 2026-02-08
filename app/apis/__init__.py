from flask_restx import Api

from .todo import ns as todo_ns

api = Api(
    version="1.0",
    title="REST API 실습 서버",
    description="학과 REST API 실습을 위한 테스트 서버입니다.",
    doc="/docs",
)

# ── 네임스페이스 등록 (시나리오 추가 시 여기에 등록) ──────────

api.add_namespace(todo_ns, path="/api/todo")
