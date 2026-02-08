from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="210.101.236.166", port=80, debug=True)
