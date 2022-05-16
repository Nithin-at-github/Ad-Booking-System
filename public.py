from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	session.clear()
	return render_template("index.html")

@public.route('/login',methods=['get','post'])
def login():
	session.clear()

	if 'login' in request.form:
		username=request.form['username']
		password=request.form['password']

		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(username,password)
		res=select(q)

		if res:
			session['log_id']=res[0]['log_id']
			if res[0]['user_type']=='admin':
				return redirect(url_for('admin.admin_home'))
			if res[0]['user_type']=='media':
				return redirect(url_for('media.media_home'))
		else:
			flash("Invalid Username or Password")

	return render_template("login.html")
