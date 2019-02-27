from flask import render_template

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

