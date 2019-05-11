import application


app = application.create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=8910, debug=True)
