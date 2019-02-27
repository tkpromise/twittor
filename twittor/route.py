from flask import render_template, redirect, url_for
from twittor.forms import LoginForm

def index():
    name = {'username':'root'}
    posts = [
        {
            'author':{'username':'root'},
            'body':'hi I\'m root!'
        },
        {
            'author':{'username':'test'},
            'body':'hi I\'m test!'
        }
    ]
    return render_template('index.html', name=name, posts=posts)

def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        msg = f'username={form.username.data}, password={form.password.data}, remember_me={form.remember_me.data}'
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

