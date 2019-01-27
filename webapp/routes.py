from flask import render_template, flash, redirect, url_for
from application import app
from webapp.forms import LoginForm
from webapp.forms import FeedForm
from flask import Flask, request, render_template

import time


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/eat')
def eat():
    return render_template('eat.html')


@app.route('/fed')
def fed():
    return render_template('fed.html')
