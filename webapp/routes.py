from flask import render_template, flash, redirect, url_for
from application import app
from webapp.forms import LoginForm
from webapp.forms import FeedForm
from webapp.call_function import call_function
from flask import Flask, request, render_template
import requests
import os


@app.route('/', methods=['GET', 'POST'])
def home():
    egg_filename = os.path.join(app.config['DINO_FOLDER'], 'egg.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'grassy_field.jpg')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/eat')
    print("not validated")
    return render_template('home.html', form=form, dino_file=egg_filename, background_image=background_file)

@app.route('/eat', methods=['GET', 'POST'])
def eat():
    # e = requests.get('https://frontsend.azurewebsites.net/').content
    user_input = "EAT"
    print(user_input)
    hatchd_filename = os.path.join(app.config['DINO_FOLDER'], 'hatched.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'grassy_field.jpg')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/fed')
    print("not validated")
    return render_template('eat.html', form=form, uin=user_input, dino_file=hatchd_filename, background_image=background_file)

@app.route('/fed', methods=['GET', 'POST'])
def fed():
    user_input = "FED"
    print(user_input)
    dino_filename = os.path.join(app.config['DINO_FOLDER'], 'dino.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'grassy_field.jpg')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/eat')
    print("not validated")
    return render_template('fed.html', form=form, uin=user_input, dino_file=dino_filename, background_image=background_file)
