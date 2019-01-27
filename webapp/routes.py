from flask import render_template, flash, redirect, url_for
from application import app
from webapp.forms import LoginForm
from webapp.forms import FeedForm
from webapp.call_function import call_function
from flask import Flask, request, render_template

@app.route('/', methods=['GET', 'POST'])
def home():
    form = FeedForm()
    if form.validate_on_submit():
        # call_function(form.user_input)
        print("validated")
        return redirect('/eat')
    print("not validated")
    return render_template('home.html', form=form)

@app.route('/eat')
def eat():
    return render_template('eat.html')

@app.route('/fed')
def fed():
    return render_template('fed.html')
