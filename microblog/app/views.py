from app import app
from flask import render_template, flash, redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Sakti'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Aishwarya'}, 
            'body': 'Good morning from SanFrancisco!' 
        },
        { 
            'author': {'nickname': 'Sakti'}, 
            'body': 'But it is a rainy day in Sunnyvale !' 
        },
        { 
            'author': {'nickname': 'Sakti'}, 
            'body': 'Flask is beginning to look like fun!' 
        }
    ]
    return render_template('index.html', title='Home',user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])