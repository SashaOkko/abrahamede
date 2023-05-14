from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    uq = {'nick':'Bek'}
    posts = [
        {
            'author':{'username':'Ivan'},
            'body': 'Привет, всем!'
        },
        {
            'author': {'username': 'sanya'},
            'body': 'https://vt.tiktok.com/ZS8cYFWSY/'
        }
        {
            'author': {'username': 'Ivan'},
            'body': 'бадон'
        }
    ]
    return render_template('aboba shih.html', title = 'Главная страница', name = 'Фруктик', uq = uq)

@app.route('/index')
def main():
    return render_template('hell.html')

if __name__=='__main__':
    app.run()

