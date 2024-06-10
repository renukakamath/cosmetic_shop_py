from flask import * 
from database import*

from datetime import date



customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():
    data={}
    customer_fname=session['customer_fname']
    data['customer_fname']=customer_fname
    return render_template('customer_home.html',data=data)


@customer.route('/customer_viewproduct',methods=['post','get'])
def customer_viewproduct():
	data={} 


	q="select * from category"
	res=select(q)
	data['cat']=res




	if 'action' in request.args:
		action=request.args['action']
		key=request.args['key']
	else:
		action=None

	# flash(action)

	
	if "search" in request.form:
		p=request.form['product']+'%'

		q="SELECT * FROM product  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN `color` USING (`color_id`) INNER JOIN `brand` USING (brand_id) where color_name like '%s' and color_status='1' or brand_name like '%s' and brand_status='1' or subcategory_name like '%s'  and sub_status='1' or product_name like '%s' and product_status='1' and and product_exp>curdate()  group by product_id "%(p,p,p,p)
		res=select(q)
		data['productsearch']=res
		
		

	else:
		if action == "search":
			# print("kkkkkkkkkk")
			q="SELECT * FROM product  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN `color` USING (`color_id`) INNER JOIN `brand` USING (brand_id)  where subcategory_id='%s'  and product_exp>curdate()"%(key)
			print(q)
			data['productsearch']=select(q)
		else:
			print("lllllllllll")
			q="SELECT * FROM product INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN `category` USING (`category_id`) INNER JOIN `color` USING (`color_id`) INNER JOIN `brand` USING (brand_id)   where product_status='1' and color_status='1' and brand_status='1' and sub_status='1' and status='1'  and rate<> 0 and product_exp>curdate() GROUP BY product_id"
			res=select(q)
			data['productsearch']=res

	return render_template('customer_viewproduct.html',data=data)


@customer.route('/customer_addtocart',methods=['post','get'])
def customer_addtocart():
	data={}
	st=request.args['stock']
	pname=request.args['pname']
	data['pname']=pname

	pdis=request.args['pdis']
	data['pdis']=pdis

	pimg=request.args['pimg']
	data['pimg']=pimg

	pamo=request.args['pamo']
	data['pamo']=pamo


	if "cart" in request.form:
		tot=request.form['total']	
		pid=request.args['pid']
		cid=session['customer_id']

		qty=request.form['quantity']	
		


		if int(st)< int(qty):
			flash('enter less quantity')
		else:


			q="select * from order_master where customer_id='%s' and order_status='pending'"%(cid)
			res=select(q)
			if res:
				omid=res[0]['order_master_id']

			else:

				q="insert into order_master values(null,'%s','0',curdate(),'pending')"%(cid)
				omid=insert(q)


			q="select * from order_details where product_id='%s' and order_master_id='%s'"%(pid,omid)
			res=select(q)
			if res:
				odid=res[0]['order_details_id']

				a=res[0]['quantity']
				qty=request.form['quantity']




				c=int(a)+int(qty)
				print(c)

				if int(c) > int(st):
					
					flash('Out Of Stock')
					return redirect(url_for('customer.customer_viewcart'))
					

				else:

		
					q="update order_details set quantity=quantity+'%s' , total_price=total_price+'%s' where order_details_id='%s'"%(qty,tot,odid)
					update(q)

			else:

				q="insert into order_details values(null,'%s','%s','%s','%s')"%(omid,pid,qty,tot)
				insert(q)

			q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(tot,omid)
			update(q)

			flash('successfully')

			return redirect(url_for('customer.customer_viewcart'))

	return render_template('customer_addtocart.html',data=data)


@customer.route('/customer_viewcart',methods=['get','post'])
def customer_viewcart():
	data={}
	cid=session['customer_id']

	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where order_status='pending' and customer_id='%s'"%(cid)
	res=select(q)
	data['len']=len(res)
	data['cart']=res
 
	if 'action' in request.args:
		action=request.args['action']
		order_master_id=request.args['omid']
		order_details_id=request.args['odid']
		price=request.args['price']
	else:
		action=None

	if action=='minus':
		q="UPDATE `order_details` SET `quantity`=`quantity`-1,total_price=total_price-'%s'  WHERE `order_details_id`='%s'"%(price,order_details_id)
		update(q)
		q="UPDATE `order_master` SET `total_amount`=`total_amount`-'%s' WHERE `order_master_id`='%s'"%(price,order_master_id)
		update(q)
		return redirect(url_for('customer.customer_viewcart'))
	if action=='add_qty':
		q="UPDATE `order_details` SET `quantity`=`quantity`+1,total_price=total_price+'%s'  WHERE `order_details_id`='%s'"%(price,order_details_id)
		update(q)
		print(q)
		q="UPDATE `order_master` SET `total_amount`=`total_amount`+'%s' WHERE `order_master_id`='%s'"%(price,order_master_id)
		print(q)
		update(q)
		return redirect(url_for('customer.customer_viewcart'))

	for i in range(1,len(res)+1):
		if 'btn'+str(i) in request.form:
			oid=request.form['oid'+str(i)]
			pid=request.form['pid'+str(i)]

			q="update order_master set total_amount=total_amount-(select total_price from order_details where product_id='%s' and order_master_id='%s') where order_master_id='%s'"%(pid,oid,oid)
			print(q)
			update(q)
			q="delete from order_details where order_master_id='%s' and product_id='%s'"%(oid,pid)
			delete(q)
			q=" select * from order_master where order_master_id='%s' and total_amount='0'"%(oid)
			ves=select(q)
			if ves:
				q="delete from order_master where order_master_id='%s'"%(oid)
				delete(q)
			flash('successfully')
			return redirect(url_for("customer.customer_viewcart"))
	return render_template('customer_viewcart.html',data=data)

@customer.route('/customer_makepayment',methods=['post','get'])	
def customer_makepayment():
	data={}
	cid=session['customer_id']

	amt=request.args['amt']
	data['amt']=amt

	q="select * from card where customer_id='%s'"%(cid)
	res=select(q)
	data['carddrop']=res
			

	if "payment" in request.form:
		ca=request.form['card']
		omid=request.args['omid']
		amt=request.args['amt']


		q="insert into payment values(null,'%s','%s','%s',curdate())"%(ca,omid,amt)
		insert(q)
		q="update order_master set order_status='Paid' where order_master_id='%s'"%(omid)
		update(q)

		# q="select * from order_details where order_master_id='%s'"%(omid)
		# res=select(q)

		# for i in res:

		# 	quantity=i['quantity']
		# 	item_id=i['product_id']
		# 	q="update product set stock=stock-'%s' where product_id='%s'"%(quantity,item_id)
		# 	update(q)

		# 	flash('successfully')

		q="select * from order_master inner join order_details using(order_master_id) inner join product using(product_id) where order_master_id='%s'"%(omid)	
		result=select(q)
		if result:
			for i in result:
				product_id=i['product_id']
				quantity=i['quantity']
				q="update product set stock=stock-'%s' where product_id='%s'"%(quantity,product_id)
				update(q)
				q="select * from product where product_id='%s' and stock='0'"%(product_id)
				
				res5=select(q)
				if res5:
					q="select * from purchase_child where product_id='%s' and pc_status='available' order by purchase_child_id desc"%(product_id)
					print(q)
					res=select(q)
					if res:
						pdid=res[0]['purchase_child_id']
						quan=res[0]['quantity']
						sellp=res[0]['selling_price']
						q="update product set rate='%s', stock='%s' where product_id='%s'"%(sellp,quan,product_id)
						print(q)
						update(q)
						q="update purchase_child set pc_status='stock added' where purchase_child_id='%s'"%(pdid)
						update(q)
					else:
						a=5
				else:
					b=4 
		# return redirect(url_for("customer.cust_home"))


		return redirect(url_for('customer.customer_viewmyorder'))

	return render_template('customer_makepayment.html',data=data,amt=amt)

@customer.route('/customer_addcard',methods=['post','get'])
def customer_addcard():

	from datetime import date

	today = date.today()
	print("Today's date:", today)


	if "card" in request.form:

		cid=session['customer_id']
		num=request.form['num']
		name=request.form['name']

		d=request.form['date']

		q="select * from card where customer_id='%s' and card_no='%s'"%(cid,num)
		res=select(q)
		if res:
			flash('already exist')

		else:


			from datetime import date,datetime

			d1=datetime.strptime(d,'%Y-%m')
			print(type(d1))


			today = datetime.today()
			print("Today's date:", type(today))

			print(d,")))))))))))")

			print(today)
			if d1 < today:
				flash('expired')
			else:
				q="insert into card values(null,'%s','%s','%s','%s') "%(cid,num,name,d)
				insert(q)
				flash('successfully')
				return redirect(url_for('customer.customer_viewcart'))
	return render_template('customer_addcard.html',today=today)	

@customer.route('/customer_viewmyorder')
def customer_viewmyorder():
	data={}
	cid=session['customer_id']

	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where  customer_id='%s' and order_status!='pending'  "%(cid)
	res=select(q)
	data['myorder']=res
	return render_template('customer_viewmyorder.html',data=data)



@customer.route('/bill1')
def bill1():
    data={}
    apid=request.args['apid']

    q="SELECT * from order_details inner join product using(product_id)  inner join order_master using(order_master_id) where order_master_id='%s' "%(apid)
    res=select(q)
    print(q)
    data['book']=res
    return render_template('bill1.html',data=data)


@customer.route('/customerprofile',methods=['get','post'])
def customerprofile():
    data={}
    cid=session['customer_id']
    q="select * from customer where customer_id='%s'"%(cid)
    res=select(q)
    print(q)
    data['book']=res
    if "cusregss" in request.form:
    	f=request.form['fname']
    	l=request.form['lname']
    	h=request.form['hno']
    	s=request.form['street']
    	di=request.form['district']
    	st=request.form['state']
    	pi=request.form['pin']
    	d=request.form['date']
    	n=request.form['num']
    	q="update customer set customer_fname='%s' ,customer_lname='%s',customer_houser_name='%s',customer_street='%s',customer_dist='%s',customer_state='%s',customer_pincode='%s',customer_dob='%s',customer_phone='%s' where customer_id='%s'"%(f,l,h,s,di,st,pi,d,n,cid)
    	update(q)
    	return redirect(url_for('customer.customerprofile'))
    return render_template('customerprofile.html',data=data)




@customer.route('/customer_addtocarts',methods=['post','get'])
def customer_addtocarts():
	data={}
	st=request.args['stock']
	pname=request.args['pname']
	data['pname']=pname

	pdis=request.args['pdis']
	data['pdis']=pdis

	pimg=request.args['pimg']
	data['pimg']=pimg

	pamo=request.args['pamo']
	data['pamo']=pamo


	if "cart" in request.form:
		tot=request.form['total']	
		pid=request.args['pid']
		cid=session['customer_id']

		qty=request.form['quantity']	
		


		if int(st)< int(qty):
			flash('enter less quantity')
		else:


			q="select * from order_master where customer_id='%s' and order_status='pending'"%(cid)
			res=select(q)
			if res:
				omid=res[0]['order_master_id']

			else:

				q="insert into order_master values(null,'%s','0',curdate(),'pending')"%(cid)
				omid=insert(q)


			q="select * from order_details where product_id='%s' and order_master_id='%s'"%(pid,omid)
			res=select(q)
			if res:
				odid=res[0]['order_details_id']

				a=res[0]['quantity']
				qty=request.form['quantity']




				c=int(a)+int(qty)
				print(c)

				if int(c) > int(st):
					
					flash('Out Of Stock')
					return redirect(url_for('customer.customer_viewcart'))
					

				else:

		
					q="update order_details set quantity=quantity+'%s' , total_price=total_price+'%s' where order_details_id='%s'"%(qty,tot,odid)
					update(q)

			else:

				q="insert into order_details values(null,'%s','%s','%s','%s')"%(omid,pid,qty,tot)
				insert(q)

			q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(tot,omid)
			update(q)

			flash('successfully')

			return redirect(url_for('customer.customer_viewcart'))

	return render_template('customer_addtocarts.html',data=data)
