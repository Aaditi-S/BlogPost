from flaskblog import app
# from flaskblog import create_app

# app = create_app()
app.app_context()
if __name__ == '__main__':
    app.run(debug=True)