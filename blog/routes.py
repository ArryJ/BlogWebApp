from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post, Comment, Rating
from blog.forms import RegistrationForm, LoginForm, CommentForm, RatingForm, SortForm
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import exc

@app.route("/")

@app.route("/home",methods=['GET','POST'])
def home():
  posts=Post.query.all()
  form = SortForm()
  if form.is_submitted():
    if form.sort_by.data == '2':
      posts = Post.query.order_by(Post.date.desc()).all()
    redirect(url_for('home'))
  return render_template('home.html',posts=posts,form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
  post=Post.query.get_or_404(post_id)
  form = CommentForm()
  form_rating = RatingForm()
  return render_template('post.html',title=post.title,post=post, form = form, form_rating= form_rating)

@app.route("/post/<int:post_id>/comment", methods= ['GET','POST'])
def addComment(post_id):
  post=Post.query.get_or_404(post_id)
  form = CommentForm()
  form_rating = RatingForm()
  if form.validate_on_submit():
    if current_user.is_authenticated:
      comment = Comment(content = form.content.data, author = current_user.id , post_id = post.id)
      db.session.add(comment)
      db.session.commit()
      flash('Comment Added')
      return redirect(url_for('post', post_id =post.id))
    else:
      flash('Please Login to comment')
  return render_template('post.html',post=post, form = form, form_rating = form_rating)

@app.route("/post/<int:post_id>/rating", methods= ['GET','POST'])
def addRating(post_id):
  post=Post.query.get_or_404(post_id)
  form = CommentForm()
  form_rating = RatingForm()
  if form_rating.validate_on_submit():
    if current_user.is_authenticated:
      rate = Rating(stars = form_rating.stars.data, author = current_user.id , post_id = post.id)
      try:
        db.session.add(rate)
        db.session.commit()
        flash('Rating Added')
      except exc.IntegrityError:
        db.session.rollback()
        flash('Cant give rating multiple times')
      
      return redirect(url_for('post', post_id =post.id))
    else:
      flash('Please Login to Rate')
    
  return render_template('post.html',post=post, form = form, form_rating = form_rating)


@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(first_name= form.first_name.data, email = form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.first_name +'!')
      return redirect(url_for('home'))
    flash('Invalid email or password.')
  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!')
  return redirect(url_for('home'))


  