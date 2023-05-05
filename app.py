from flask import Flask

app = Flask(__name__)

@app.get('/')
def Home():
    return 'Hello Home page'



@app.get('/about')
def About():
    return 'Hello About page'


if __name__ == '__app__':
    app.run()