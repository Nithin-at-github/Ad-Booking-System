from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/admin_home',methods=['get','post'])
def admin_home():
	if session.get('log_id'):
		return render_template("admin_home.html")
	else:
		return redirect(url_for('public.login'))
	
@admin.route('/admin_manage_adcategories',methods=['get','post'])
def admin_manage_adcategories():
	if session.get('log_id'):
		data={}
		q="SELECT * FROM `category`"
		res=select(q)
		data['categories']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM `category` WHERE `category_id`='%s'"%(id)
			delete(q)
			return redirect(url_for('admin.admin_manage_adcategories'))
		if action=='update':
			q="SELECT * FROM `category`WHERE `category_id`='%s'"%(id)
			res=select(q)
			data['catupdate']=res
		if 'addcat' in request.form:
			cat_name=request.form['cat_name']
			cat_desc=request.form['cat_desc']
			q="INSERT INTO `category` VALUES(NULL,'%s','%s')"%(cat_name,cat_desc)
			insert(q)
			return redirect(url_for('admin.admin_manage_adcategories'))
		if 'updatecat' in request.form:
			cat_name=request.form['cat_names']
			cat_desc=request.form['cat_descs']
			q="UPDATE `category` SET `category_name`='%s',`description`='%s' WHERE `category_id`='%s'"%(cat_name,cat_desc,id)
			update(q)
			return redirect(url_for('admin.admin_manage_adcategories'))
		return render_template("admin_manage_adcategories.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_manage_medias',methods=['get','post'])
def admin_manage_medias():
	if session.get('log_id'):
		data={}
		q="SELECT * FROM `category`"
		res=select(q)
		data['categories']=res
		q="SELECT *,`medias`.`description` AS Description  FROM `medias` INNER JOIN `category` USING(`category_id`)"
		res=select(q)
		data['medias']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM `login` WHERE `log_id`=(SELECT `log_id` FROM `medias` WHERE `media_id`='%s')"%(id)
			delete(q)
			q="DELETE FROM  `medias` WHERE `media_id`='%s'"%(id)
			delete(q)
			return redirect(url_for('admin.admin_manage_medias'))
		if action=='update':
			q="SELECT * FROM `medias` WHERE `media_id`='%s'"%(id)
			res=select(q)
			data['mediaupdate']=res
		if 'addmeds' in request.form:
			mname=request.form['mnames']
			email=request.form['emails']
			phone=request.form['phones']
			cat_id=request.form['cat_ids']
			desc=request.form['descs']
			q="UPDATE `medias` SET `media_name`='%s',`email`='%s',`phone`='%s',`category_id`='%s',`description`='%s' WHERE `media_id`='%s'"%(mname,email,phone,cat_id,desc,id)
			update(q)
			return redirect(url_for('admin.admin_manage_medias'))
		if 'addmed' in request.form:
			mname=request.form['mname']
			email=request.form['email']
			phone=request.form['phone']
			cat_id=request.form['cat_id']
			desc=request.form['desc']
			password=request.form['password']
			q="INSERT INTO `login` VALUES(NULL,'%s','%s','media')"%(email,password)
			ids=insert(q)
			q="INSERT INTO `medias` VALUES(NULL,'%s','%s','%s','%s','%s','%s')"%(ids,mname,email,phone,cat_id,desc)
			insert(q)
			return redirect(url_for('admin.admin_manage_medias'))
		return render_template("admin_manage_medias.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_userss',methods=['get','post'])
def admin_view_userss():
	if session.get('log_id'):
		data={}
		q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`)  AS NAME FROM `users`"
		res=select(q)
		data['users']=res

		return render_template("admin_view_userss.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_manage_commission',methods=['get','post'])
def admin_manage_commission():
	if session.get('log_id'):
		data={}
		q="SELECT * FROM `category`"
		res=select(q)
		data['categories']=res
		q="SELECT * FROM `commission` INNER JOIN `category` USING(`category_id`)"
		res=select(q)
		data['commission']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="DELETE FROM`commission` WHERE `commission_id`='%s'"%(id)
			delete(q)
			return redirect(url_for('admin.admin_manage_commission'))
		if action=='update':
			q="SELECT * FROM `commission` WHERE `commission_id`='%s'"%(id)
			res=select(q)
			data['commupdate']=res
		if 'submits' in request.form:
			cat_ids=request.form['cat_idss']
			percentage=request.form['percentages']
			type=request.form['types']

			q="UPDATE `commission` SET `category_id`='%s',`percentage`='%s',`type`='%s' WHERE `commission_id`='%s'"%(cat_ids,percentage,type,id)
			update(q)
			return redirect(url_for('admin.admin_manage_commission'))
		if 'submit' in request.form:
			cat_ids=request.form['cat_ids']
			percentage=request.form['percentage']
			type=request.form['type']
			q="INSERT INTO `commission` VALUES(NULL,'%s','%s','%s')"%(cat_ids,percentage,type)
			insert(q)
			return redirect(url_for('admin.admin_manage_commission'))
		return render_template("admin_manage_commission.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_media_adspace',methods=['get','post'])
def admin_view_media_adspace():
	if session.get('log_id'):
		data={}
		q="SELECT *,`adspaces`.`description` AS Description  FROM `adspaces` INNER JOIN `medias` USING(`media_id`)"
		res=select(q)
		data['adspace']=res

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=='appove':
			q="UPDATE `adspaces` SET `status`='Approved' WHERE `ad_space_id`='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_media_adspace'))

		if action=='reject':
			q="UPDATE `adspaces` SET `status`='Rejected' WHERE `ad_space_id`='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_media_adspace'))

		return render_template("admin_view_media_adspace.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_customer_booking',methods=['get','post'])
def admin_view_customer_booking():
	if session.get('log_id'):
		data={}
		id=request.args['id']
		q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME FROM `users` INNER JOIN `adcontent` USING(`user_id`) INNER JOIN `adspaces`ON `adcontent`.`ad_id`=`adspaces`.`ad_space_id` WHERE `adcontent`.`ad_type`='space' AND `ad_space_id`='%s'"%(id)
		res=select(q)
		data['cbook']=res

		return render_template("admin_view_customer_booking.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_payments',methods=['get','post'])
def admin_view_payments():
	if session.get('log_id'):
		data={}
		q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME  FROM `payment` INNER JOIN `users`  USING(`user_id`) WHERE `ad_type`='space'"
		res=select(q)
		data['payments']=res

		return render_template("admin_view_payments.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_custom_request_from_customer',methods=['get','post'])
def admin_view_custom_request_from_customer():
	if session.get('log_id'):
		data={}
		q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME FROM `customrequest` INNER JOIN `users` USING(`user_id`)INNER JOIN `category` USING(`category_id`) INNER JOIN `adcontent` ON `customrequest`.`request_id`=`adcontent`.`ad_id`  WHERE `adcontent`.`ad_type`='custom' "
		res=select(q)
		data['crequest']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='approvestat':
			q="UPDATE `customrequest` SET `request_status`='Accepted by Admin' WHERE `request_id`='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_custom_request_from_customer'))
		if action=='rejectstat':
			q="UPDATE `customrequest` SET `request_status`='Rejected by Admin' WHERE `request_id`='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_custom_request_from_customer'))

		return render_template("admin_view_custom_request_from_customer.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():
	if session.get('log_id'):
		data={}
		login_id=session['log_id']
		q="SELECT *,CONCAT(`first_name`,' ',`middle_name`,' ',`last_name`) AS NAME FROM `complaint` INNER JOIN `users` USING(`user_id`)"
		res=select(q)
		data['comments']=res
		j=0
		for i in range(1,len(res)+1):
			print('submit'+str(i))
			if 'submit'+str(i) in request.form:
				reply=request.form['reply'+str(i)]
				print(res[j]['complaint_id'])
				q="UPDATE `complaint` SET `solution_description`='%s' WHERE `complaint_id`='%s'"%(reply,res[j]['complaint_id'])
				update(q)
				return redirect(url_for('admin.admin_view_complaints')) 	
			j=j+1
		
		return render_template("admin_view_complaints.html",data=data)
	else:
		return redirect(url_for('public.login'))

@admin.route('/admin_settings',methods=['get','post'])
def admin_settings():
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