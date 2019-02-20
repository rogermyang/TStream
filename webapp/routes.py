from flask import render_template, flash, redirect, url_for
from flask_app import app
from webapp.forms import LoginForm
from webapp.forms import FeedForm
from webapp.call_function import call_function
from flask import Flask, request, render_template
import requests
import os
from generator.generate import generate_tweet


@app.route('/', methods=['GET', 'POST'])
def home():
    egg_filename = os.path.join(app.config['DINO_FOLDER'], 'egg.png')
    poopimg = os.path.join(app.config['DINO_FOLDER'], 'poop.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'back1.jpg')
    cred_path = os.path.join(app.config['CRED_PATH'], 'twt_creds')
    form = FeedForm()
    if form.validate_on_submit():
        # print("validated")
        form_list = form.user_input.data.split(" ")

        print("\n\n\n\n\n\n\n\n")
        print(form_list)

        generate_tweet(cred_path, form_list)
        return redirect('/eat')
    # print("not validated")
    return render_template('home.html', form=form, dino_file=egg_filename, background_image=background_file)

@app.route('/eat', methods=['GET', 'POST'])
def eat():
    # e = requests.get('https://frontsend.azurewebsites.net/').content
    user_input = "EAT"
    print(user_input)
    hatchd_filename = os.path.join(app.config['DINO_FOLDER'], 'hatched1.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'back1.jpg')
    poopimg = os.path.join(app.config['DINO_FOLDER'], 'poop.png')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/fed')
    print("not validated")
    return render_template('eat.html', form=form, uin=user_input, dino_file=hatchd_filename, poop=poopimg, background_image=background_file)

@app.route('/fed', methods=['GET', 'POST'])
def fed():
    user_input = "FED"
    print(user_input)
    dino_filename = os.path.join(app.config['DINO_FOLDER'], 'dino.png')
    background_file = os.path.join(app.config['BACKGROUND_FOLDER'], 'back1.jpg')
    poopimg = os.path.join(app.config['DINO_FOLDER'], 'poop.png')
    form = FeedForm()
    if form.validate_on_submit():
        print("validated")
        return redirect('/eat')
    print("not validated")
    return render_template('fed.html', form=form, uin=user_input, dino_file=dino_filename, poop=poopimg, background_image=background_file)
