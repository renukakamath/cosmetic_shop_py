from flask import *
from database import*

courier=Blueprint('courier',__name__)

@courier.route('/courier_home')
def courier_home():

	return render_template('courier_home.html')

@courier.route('/courier_viewbookings')
def courier_viewbookings():
	data={}
	cid=session['courier_id']

	if "action" in request.args:
		action=request.args['action']
		oid=request.args['oid']
	else:
		action=None

	if action=='picked':
		q="update order_master set order_status='Picked' where order_master_id='%s'"%(oid)
		update(q)
		q="update delivery set status='Picked' where order_master_id='%s'"%(oid)
		update(q)
  
		flash('successfully')
		return redirect(url_for('courier.courier_viewbookings'))

	if action=='Delivered':

		q="update delivery set status='Delivered' where order_master_id='%s'"%(oid)
		update(q)
		q="update order_master set order_status='Delivered' where order_master_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('courier.courier_viewbookings'))

			
	q="select * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (`customer_id`)   inner join subcategory using (subcategory_id) inner join brand using (brand_id) inner join color using (color_id) inner join delivery using(order_master_id) where (courier_id='%s' and order_status='Paid') or (courier_id='%s' and order_status='Picked') or (courier_id='%s' and order_status='Delivered' )  OR (courier_id='%s' AND order_status='Assign' )   group by order_master_id "%(cid,cid,cid,cid)
	res=select(q)
	data['book']=res

	return render_template('courier_viewbookings.html',data=data)	


	