from flask import render_template
from app import app


@app.route("/")
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [
        # fake array of posts#
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='home',
                           user=user,
                           posts=posts

                           )
