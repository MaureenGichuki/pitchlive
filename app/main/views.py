from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Comment,Pitch
from .forms import UpdateProfile,CommentForm,PitchForm

from .. import db


@main.route('/')
def index():
    '''
    root page function that returns the index page

    '''
    return render_template('index.html')

@main.route('/health')
def heal():

    pitches=Pitch.get_pitches(id)
    return render_template('health.html',pitches=pitches)

@main.route('/fitness')
def fit():

    pitches=Pitch.get_pitches(id)
    return render_template('fitness.html',pitches=pitches)

@main.route('/technology')
def tech():
   
    pitches=Pitch.get_pitches(id)
    return render_template('technology.html')

@main.route('/career')
def car():

    pitches=Pitch.get_pitches(id)
    return render_template('career.html',pitches=pitches)


@main.route('/health/pitch',methods= ['GET','POST'])
@login_required
def healthpitch():

    form=PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch=form.pitch.data
        new_pitch=Pitch(title=title,pitch=pitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.heal'))

    return render_template('pitch.html',pitch_form=form)

@main.route('/fitness/pitch',methods= ['GET','POST'])
@login_required
def fitnesspitch():
   
    form=PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch=form.pitch.data
        new_pitch=Pitch(title=title,pitch=pitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.fit'))

    return render_template('pitch.html',pitch_form=form)

@main.route('/technology/pitch',methods= ['GET','POST'])
@login_required
def techpitch():
   
    form=PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch=form.pitch.data
        new_pitch=Pitch(title=title,pitch=pitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.tech'))

    return render_template('pitch.html',pitch_form=form)

@main.route('/career/pitch',methods= ['GET','POST'])
@login_required
def careerpitch():
   
    form=PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch=form.pitch.data
        new_pitch=Pitch(title=title,pitch=pitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.car'))

    return render_template('pitch.html',pitch_form=form)




@main.route('/health/comment',methods= ['GET','POST'])
@login_required
def health_comment():

    form = CommentForm()

    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.heal'))


    return render_template('comment.html',comment_form=form,comment=comments)


@main.route('/fitness/comment',methods= ['GET','POST'])
@login_required
def fitness_comment():

    form = CommentForm()

    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.tech'))



    return render_template('comment.html',comment_form=form)


@main.route('/career/comment',methods= ['GET','POST'])
@login_required
def career_comment():

    form = CommentForm()
    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.car'))



    return render_template('comment.html',comment_form=form)

@main.route('/technology/comment',methods= ['GET','POST'])
@login_required
def technology_comment():

    form = CommentForm()
    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.tech'))



    return render_template('comment.html',comment_form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

