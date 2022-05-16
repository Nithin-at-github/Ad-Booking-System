from flask import *
from database import *
import uuid
media=Blueprint('media',__name__)

@media.route('/media_home',methods=['get','post'])
def media_home():
	if session.get('log_id'):
		return render_template("media_home.html")
	else:
		return redirect(url_for('public.login'))

@media.route('/media_manage_adspaces',methods=['get','post'])
def media_manage_adspaces():
	if session.get('log_id'):
		data={}
		if 'action' in request.args:
			id=request.args['id']
			action=request.args['action']
		else:
			action=None
		if action=='update':
			q="SELECT * FROM `adspaces` WHERE `ad_space_id`='%s'"%(id)
			res=select(q)
			data['updateamnt']=res
			print(res)
		if 'update' in request.form:
			amounts=request.form['amounts']
			q="UPDATE `adspaces` SET `amount`='%s' WHERE `ad_space_id`='%s'"%(amounts,id)
			update(q)
			return(redirect(url_for('media.media_manage_adspaces')))
		ids=session['log_id']
		q="SELECT * FROM `adspaces` WHERE `media_id`=(SELECT `media_id` FROM `medias` WHERE `log_id`='%s')"%(ids)
		res=select(q)

		data['adspace']=res
		if 'adspace' in request.form:
			description=request.form['description']
			amount=request.form['amount']
			q="INSERT INTO `adspaces` VALUES(NULL,(SELECT `media_id` FROM `medias` WHERE `log_id`='%s'),'%s','%s','pending')"%(ids,description,amount)
			insert(q)
			return redirect(url_for('media.media_manage_adspaces'))
		return render_template("media_manage_adspaces.html",data=data)
	else:
		return redirect(url_for('public.login'))

@media.route('/media_view_customer_requests',methods=['get','post'])
def media_view_customer_requests():
	if session.get('log_id'):
		data={}
		if 'id' in request.args:
			id=request.args['id']
			q="SELECT *,`adcontent`.`status` AS stat,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME FROM `adspaces` INNER JOIN `adcontent`ON `adspaces`.`ad_space_id`=`adcontent`.`ad_id` INNER JOIN `users` USING(`user_id`)  WHERE `ad_id`='%s' AND `ad_type`='space'"%(id)
			res=select(q)
			print(q)

			data['cmrreq']=res
		if 'ids' in request.args:
			ids=request.args['ids']
			q="UPDATE `adspaces` SET `status`='Approved' WHERE `ad_space_id`='%s'"%(ids)
			update(q)
			print(q)
			q="UPDATE `adcontent` SET `status`='Approved' WHERE `ad_id`='%s' AND `ad_type`='space'"%(ids)
			update(q)
			print(q)
			return redirect(url_for('media.media_manage_adspaces'))

		return render_template("media_view_customer_requests.html",data=data)
	else:
		return redirect(url_for('public.login'))

@media.route('/media_view_payments',methods=['get','post'])
def media_view_payments():
	if session.get('log_id'):
		data={}
		if 'ids' in request.args:
			ids=request.args['ids']
			q="SELECT * FROM `payment` WHERE `ad_id`='%s' AND `ad_type`='space'"%(ids)
			res=select(q)
			data['spacepay']=res

		return render_template("media_view_payments.html",data=data)
	else:
		return redirect(url_for('public.login'))

@media.route('/media_view_custom_requests',methods=['get','post'])
def media_view_custom_requests():
	if session.get('log_id'):
		data={}
		ids=session['log_id']
		q="SELECT * FROM `customrequest` INNER JOIN `adcontent` ON `customrequest`.`request_id`=`adcontent`.`ad_id` INNER JOIN `category` USING(`category_id`) WHERE ad_type='custom' AND `request_status`='Accepted by Admin'"
		res=select(q)
		data['customreq']=res
		print(res)
		
		if 'ids' in request.args:
			id=request.args['ids']
			q="SELECT * FROM `customrequest` WHERE `request_id`='%s'"%(id)
			res=select(q)
			data['staass']=res
		return render_template("media_view_custom_requests.html",data=data)
	else:
		return redirect(url_for('public.login'))

@media.route('/media_manage_custom_amount',methods=['get','post'])
def media_manage_custom_amount():
	if session.get('log_id'):
		data={}
		if 'id' in request.args:
			id=request.args['id']
			
			q="SELECT * FROM `payment` WHERE `ad_id`='%s' AND `ad_type`='custom'"%(id)
			res=select(q)
			print(q)
			data['pays']=res
			q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME FROM `users` WHERE `user_id`=(SELECT `user_id` FROM `customrequest` WHERE `request_id`='%s')"%(id)
			res=select(q)
			data['users']=res

			if 'amounts' in request.form:
				ad_amount=request.form['ad_amount']
				net_amount=request.form['net_amount']
				q="INSERT INTO `payment` VALUES(NULL,(SELECT `user_id` FROM `customrequest` WHERE `request_id`='%s'),CURDATE(),'%s','custom','%s','%s','pending')"%(id,id,ad_amount,net_amount)
				insert(q)
				print(q)
				return redirect(url_for('media.media_manage_custom_amount'))
		return render_template("media_manage_custom_amount.html",data=data)
	else:
		return redirect(url_for('public.login'))
	
@media.route('/media_settings',methods=['get','post'])
def media_settings():
	if session.get('log_id'):
		data={}
		if 'reset' in request.form:
			pas=request.form['pass']
			npass=request.form['npass']
			cpass=request.form['cpass']
			if npass==cpass:
				q="SELECT * FROM `login` WHERE `log_id`='%s'"%(session.get('log_id'))
				data['pas']=select(q)
				if pas == data['pas'][0]['password']:
					q="UPDATE `login` SET `password`='%s' WHERE `log_id`='%s'"%(cpass,session.get('log_id'))
					update(q)
					flash("Password reseted Successfully")
				else:
					flash("Current password not matching..!")
			else:
				flash("Passwords not matching..!")
		return render_template('admin_settings.html')
	else:
		return redirect(url_for('public.login'))
