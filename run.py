import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("HOST", "210.101.236.166")
    port = int(os.environ.get("PORT", 80))
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    app.run(host=host, port=port, debug=debug)
