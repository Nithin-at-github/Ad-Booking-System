from flask import Blueprint,render_template,redirect,url_for,session,request
from database import*
import uuid
import demjson
api=Blueprint('api',__name__)
@api.route('/login/',methods=['get','post'])
def login():
	data={}
	data.update(request.args)
	username = request.args['username']
	password = request.args['password']
	q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(username,password)
	res = select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)
@api.route('/register/',methods=['get','post'])
def register():
	data={}
	first=request.args['fname']
	last=request.args['lname']
	midname=request.args['mname']

	dob=request.args['dob']
	email=request.args['email']
	phn=request.args['phone']



	house=request.args['hname']
	place=request.args['place']

	pin=request.args['pincode']
	
	district=request.args['district']


	user=request.args['username']
	pas=request.args['password']
	q="INSERT INTO `login` VALUES(NULL,'%s','%s','user')"%(user,pas)
	ids=insert(q)
	q="INSERT INTO `users` VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ids,first,last,midname,dob,email,phn,house,place,district,pin)
	insert(q)
	data['status']  = 'success'
	return  demjson.encode(data)


@api.route('/categories/',methods=['get','post'])
def categories():
	data={}
	q="SELECT * FROM `category`"
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)
@api.route('/media/',methods=['get','post'])
def media():
	data={}
	q="SELECT * FROM `medias` INNER JOIN `category`"
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)
@api.route('/adspaces/',methods=['get','post'])
def adspaces():

	data={}
	media_id=request.args['media_id']
	q="SELECT * FROM `adspaces` INNER JOIN `medias` USING(`media_id`) WHERE `media_id`='%s' AND `adspaces`.`status`='pending'"%(media_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)


@api.route('/booking/',methods=['get','post'])
def booking():
	data={}
	print("hiii")
	image=request.files['image']
	print(image)

	path='static/images/'+str(uuid.uuid4())+image.filename
	image.save(path)
	print(path)
	message=request.form['message']
	ad_space_id=request.form['ad_space_id']
	log_id=request.form['log_id']
	print(message)
	print(ad_space_id)
	print(log_id)
	q="INSERT INTO `adcontent` VALUES(NULL,'%s',(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'space',CURDATE(),'%s','%s','pending')"%(ad_space_id,log_id,path,message)
	print(q)
	insert(q)
	q="UPDATE `adspaces` SET `status`='Booked' WHERE `ad_space_id`='%s'"%(ad_space_id)
	update(q)
	data['status']  = 'success'


	return  demjson.encode(data)
@api.route('/adspacess/',methods=['get','post'])
def adspacess():

	data={}
	log_id=request.args['log_id']
	q="SELECT *,`adspaces`.`status` AS stat FROM `adspaces` INNER JOIN `adcontent` ON `adcontent`.`ad_id`=`adspaces`.`ad_space_id` WHERE `adspaces`.`status`='Booked' AND `user_id`=(SELECT `user_id` FROM `users` WHERE `log_id`='%s')"%(log_id)
	res=select(q)
	print(res)
	print(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)
@api.route('/payment/',methods=['get','post'])
def payment():

	data={}
	log_id=request.args['log_id']
	ad_space_id=request.args['ad_space_id']
	q="SELECT `percentage` FROM  `commission` WHERE `category_id`=(SELECT `category_id` FROM `medias` WHERE `media_id`=(SELECT `media_id` FROM `adspaces` WHERE `ad_space_id`='%s')) AND `type`='space'"%(ad_space_id)
	res=select(q)
	print(res)
	percentage=res[0]['percentage']
	
	print(q)
	q="SELECT * FROM `adspaces` WHERE `ad_space_id`='%s'"%(ad_space_id)
	res=select(q)
	amount=res[0]['amount']
	print(amount,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
	netamount=int(amount)+(int(amount)/10)
	print(netamount)

	print(res)
	if(len(res) > 0):
		data['netamount']=netamount
		data['amount']=amount
		data['status']  = 'success'
		
	else:
		data['status']	= 'failed'
	data['method']='pay'
	return  demjson.encode(data)

@api.route('/payments/',methods=['get','post'])
def payments():

	data={}
	log_id=request.args['log_id']
	ad_space_id=request.args['ad_space_id']
	amount=request.args['amnt']
	netamount=request.args['ntamnt']
	q="INSERT INTO `payment` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),CURDATE(),'%s','space','%s','%s','cash')"%(log_id,ad_space_id,amount,netamount)
	insert(q)

	print(q)
	data['method']='pays'

	data['status']  = 'success'
		
	
	return  demjson.encode(data)

	
@api.route('/category/',methods=['get','post'])
def category():

	data={}
	log_id=request.args['log_id']
	q="SELECT *FROM `customrequest` WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `log_id`='%s')"%(log_id)
	ress=select(q)

	q="SELECT * FROM `category`"
	res=select(q)
	print(res)
	print(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['requests']=ress
		data['data'] = res
		data['method']='category'
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)


@api.route('/crequest/',methods=['get','post'])
def crequest():

	data={}
	log_id=request.args['log_id']
	description=request.args['description']
	cid=request.args['cid']
	
	
	q="INSERT INTO `customrequest` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'%s','%s','pending',CURDATE(),'0')"%(log_id,cid,description)
	insert(q)

	print(q)
	data['method']='creq'

	data['status']  = 'success'
		
	
	return  demjson.encode(data)


@api.route('/bookings/',methods=['get','post'])
def bookings():
	data={}
	print("hiii")
	image=request.files['image']
	print(image)

	path='static/images/'+str(uuid.uuid4())+image.filename
	image.save(path)
	print(path)
	message=request.form['message']
	req_id=request.form['req_id']
	log_id=request.form['log_id']
	print(message)
	print(req_id)
	print(log_id)
	q="INSERT INTO `adcontent` VALUES(NULL,'%s',(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'custom',CURDATE(),'%s','%s','pending')"%(req_id  ,log_id,path,message)
	print(q)
	insert(q)
	q="UPDATE `customrequest` SET `request_status`='Waiting for Approval' WHERE `request_id`='%s'"%(req_id)
	update(q)
	data['status']  = 'success'


	return  demjson.encode(data)
@api.route('/cusspace/',methods=['get','post'])
def cusspace():

	data={}
	log_id=request.args['log_id']
	q="SELECT * FROM `customrequest` INNER JOIN `adcontent` ON `adcontent`.`ad_id`=`customrequest`.`request_id` WHERE `adcontent`.`ad_type`='custom' AND `adcontent`.`user_id`=(SELECT `user_id` FROM `users` WHERE `log_id`='%s')"%(log_id)
	res=select(q)
	print(res)
	print(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  demjson.encode(data)
@api.route('/paymentss/',methods=['get','post'])
def paymentss():

	data={}
	log_id=request.args['log_id']
	ad_space_id=request.args['ad_space_id']
	q="SELECT * FROM `payment` WHERE  `ad_id`='%s'  AND `ad_type`='custom'"%(ad_space_id)
	res=select(q)
	if(len(res) > 0):
		data['netamount']=res[0]['net_amount']
		data['amount']=res[0]['ad_amount']
		data['status']  = 'success'
		
	else:
		data['status']	= 'failed'
	data['method']='pay'
	
	
	return  demjson.encode(data)



@api.route('/booked/',methods=['get','post'])
def booked():

	data={}
	log_id=request.args['log_id']
	ad_space_id=request.args['ad_space_id']
	
	
	
	q="UPDATE `payment` SET `payment_type` ='paid' WHERE `ad_id`='%s' AND `ad_type`='custom'"%(ad_space_id)
	update(q)
	q="UPDATE `adcontent` SET `status`='Booked' WHERE `ad_id`='%s' AND `ad_type`='custom'"%(ad_space_id)
	update(q)
	print(q)
	data['method']='pays'

	data['status']  = 'success'
		
	
	return  demjson.encode(data)
@api.route('/scomp/',methods=['get','post'])
def scomp():
	data={}
	log_id=request.args['log_id']
	
	message=request.args['complaint']

	q="INSERT INTO `complaint` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `log_id`='%s'),'%s','pending',CURDATE())"%(log_id,message)
	insert(q)
	data['status']  = 'success'
	data['method']='smessage'
	return demjson.encode(data)
@api.route('/vcomp/',methods=['get','post'])
def vcomp():
	data={}
	log_id=request.args['log_id']

	q="SELECT * FROM `complaint` WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `log_id`='%s')"%(log_id)
	print(q)
	res = select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='vmessage'
	
	return demjson.encode(data)
