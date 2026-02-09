import time
from flask_restx import Namespace, Resource, fields

ns = Namespace("todo", description="To-Do 관련 API")

# ── Swagger 모델 정의 ──────────────────────────────────────────

todo_input = ns.model("TodoInput", {
    "text": fields.String(required=True, description="할 일 내용", example="장보기"),
})

todo_update = ns.model("TodoUpdate", {
    "text": fields.String(description="할 일 내용", example="장보기"),
    "completed": fields.Boolean(description="완료 여부", example=True),
})

todo_model = ns.model("Todo", {
    "id": fields.Integer(description="고유 ID", example=1738900000000),
    "text": fields.String(description="할 일 내용", example="장보기"),
    "completed": fields.Boolean(description="완료 여부", example=False),
})

# ── 인메모리 저장소 ────────────────────────────────────────────

todos_db = {}
_last_id = 0


def _generate_id():
    """밀리초 타임스탬프 기반 ID를 생성한다. 동일 밀리초 충돌을 방지한다."""
    global _last_id
    new_id = int(time.time() * 1000)
    if new_id <= _last_id:
        new_id = _last_id + 1
    _last_id = new_id
    return new_id


def get_user_todos(user_id):
    if user_id not in todos_db:
        todos_db[user_id] = []
    return todos_db[user_id]


def parse_todo_id(raw):
    """todo_id 문자열을 정수로 변환하고, 실패 시 400 에러를 반환한다."""
    try:
        return int(raw)
    except (ValueError, TypeError):
        ns.abort(400, "todo_id must be a number")


# ── API 엔드포인트 ─────────────────────────────────────────────

@ns.route("/<string:user_id>/todos")
@ns.param("user_id", "사용자 ID (예: alice, bob)")
class TodoList(Resource):

    @ns.doc("할 일 목록 조회")
    @ns.marshal_list_with(todo_model)
    def get(self, user_id):
        """해당 사용자의 전체 할 일 목록을 반환합니다."""
        return todos_db.get(user_id, [])

    @ns.doc("할 일 추가")
    @ns.expect(todo_input)
    @ns.marshal_with(todo_model, code=201)
    def post(self, user_id):
        """새로운 할 일을 추가합니다."""
        data = ns.payload
        if not isinstance(data, dict):
            ns.abort(400, "request body must be a JSON object")
        text = data.get("text")

        if not isinstance(text, str) or not text.strip():
            ns.abort(400, "text(string) is required")

        todo = {
            "id": _generate_id(),
            "text": text.strip(),
            "completed": False,
        }
        get_user_todos(user_id).append(todo)
        return todo, 201


@ns.route("/<string:user_id>/todos/<string:todo_id>")
@ns.param("user_id", "사용자 ID")
@ns.param("todo_id", "할 일 ID")
class TodoItem(Resource):

    @ns.doc("할 일 수정")
    @ns.expect(todo_update)
    @ns.marshal_with(todo_model)
    def patch(self, user_id, todo_id):
        """할 일의 내용이나 완료 상태를 수정합니다."""
        todo_id = parse_todo_id(todo_id)
        data = ns.payload
        if not isinstance(data, dict):
            ns.abort(400, "request body must be a JSON object")
        todos = todos_db.get(user_id, [])
        todo = next((t for t in todos if t["id"] == todo_id), None)

        if todo is None:
            ns.abort(404, "todo not found")

        if "completed" in data:
            if not isinstance(data["completed"], bool):
                ns.abort(400, "completed must be a boolean (true/false)")
            todo["completed"] = data["completed"]
        if "text" in data:
            if not isinstance(data["text"], str) or not data["text"].strip():
                ns.abort(400, "text must be a non-empty string")
            todo["text"] = data["text"].strip()

        return todo

    @ns.doc("할 일 삭제")
    def delete(self, user_id, todo_id):
        """할 일을 삭제합니다."""
        todo_id = parse_todo_id(todo_id)
        todos = todos_db.get(user_id, [])
        todo = next((t for t in todos if t["id"] == todo_id), None)

        if todo is None:
            ns.abort(404, "todo not found")

        todos.remove(todo)
        return {"message": "deleted"}, 200


@ns.route("/users")
class UserList(Resource):

    @ns.doc("사용자 목록 조회")
    def get(self):
        """등록된 전체 사용자와 할 일 개수를 반환합니다."""
        return {uid: len(todos) for uid, todos in todos_db.items()}
