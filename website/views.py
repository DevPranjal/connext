from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Interests, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('Note is too short!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note added!', category='success')
    counts = []
    for interest in current_user.interests:
        query =  Interests.query.filter_by(data=interest.data)
        current_count = query.count() - 1
        counts.append(current_count)
    return render_template("home.html", user=current_user, counts=counts)


@views.route('/interests', methods=['GET', 'POST'])
@login_required
def interests():
    if request.method == 'POST':
        interests_form = request.form
        loi = interests_form.getlist("interests")

        if len(loi) < 1:
            flash('Select atleast one interest', category='error')
        else:
            for interest in loi:
                current_interest = Interests(data=interest, user_id=current_user.id)
                db.session.add(current_interest)
                db.session.commit()
            flash('Interests added!', category='success')
            return redirect(url_for('views.home'))

    return render_template("interests.html", user=current_user)


@views.route('/competetive-programming')
def competetive_programming():
    user_list = []
    query =  Interests.query.filter_by(data="Competetive-Programming")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Competetive-Programming.html", user=current_user, people=user_list)


@views.route('/finance')
def finance():
    user_list = []
    query =  Interests.query.filter_by(data="Finance")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Finance.html", user=current_user, people=user_list)


@views.route('/design')
def design():
    user_list = []
    query =  Interests.query.filter_by(data="Design")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Design.html", user=current_user, people=user_list)


@views.route('/data-science')
def data_science():
    user_list = []
    query =  Interests.query.filter_by(data="Data-Science")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Data-Science.html", user=current_user, people=user_list)
 

@views.route('/web-development')
def web_development():
    user_list = []
    query =  Interests.query.filter_by(data="Web-Development")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Web-Development.html", user=current_user, people=user_list)


@views.route('/android-development')
def android_development():
    user_list = []
    query =  Interests.query.filter_by(data="Android-Development")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Android-Development.html", user=current_user, people=user_list)


@views.route('/music')
def music():
    user_list = []
    query =  Interests.query.filter_by(data="Music")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Music.html", user=current_user, people=user_list)


@views.route('/video-editing')
def video_editing():
    user_list = []
    query =  Interests.query.filter_by(data="Video-Editing")
    for interest in query:
        if current_user.id != interest.user_id:
            user_list.append(User.query.filter_by(id=interest.user_id).first())

    return render_template("Video-Editing.html", user=current_user, people=user_list)