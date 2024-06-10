from flask import * 
from database import*
import uuid



staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():

	return render_template('staff_home.html')



@staff.route('/staff_managevendor',methods=['post','get'])	
def staff_managevendor():
	data={}
	q="select * from vendor"
	res=select(q)
	data['vendorview']=res


	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None

	if action=='inactive':
		q="update vendor set vendor_status='0' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))

	if action=='active':
		q="update vendor set vendor_status='1' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))

	if action=='update':
		q="select * from vendor where vendor_id='%s'"%(vid)
		res=select(q)
	
		data['vendorupdate']=res

	if "up" in request.form:
		f=request.form['fname']
		n=request.form['num']
		e=request.form['email']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		p=request.form['pin']
		d=request.form['date']
		q="update vendor set vendor_name='%s',vendor_phone='%s',vendor_email='%s',vendor_hno='%s',vendor_street='%s',vendor_dist='%s',vendor_pin='%s',vendor_date='%s' where vendor_id='%s'"%(f,n,e,h,s,di,p,d,vid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('staff.staff_managevendor'))
		
			

	if "vendor" in request.form:
	
		f=request.form['fname']
		n=request.form['num']
		e=request.form['email']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		p=request.form['pin']
		d=request.form['date']
		q="insert into vendor values(null,'0','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(f,n,e,h,s,di,p,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))
	return render_template('/staff_managevendor.html',data=data)

@staff.route('/staff_managecourier',methods=['post','get'])
def staff_managecourier():
	data={}
	q="select * from courier inner join login using (username)"
	res=select(q)
	data['courierview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='update':
		q="select * from courier where username='%s'"%(cid)
		res=select(q)

		data['courierupdate']=res



	if "update" in request.form:
		f=request.form['fname']
		s=request.form['street']
		d=request.form['district']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		q="update  courier set courier_name='%s', courier_street='%s',courier_dist='%s',courier_state='%s',courier_pincode='%s',courier_phone='%s',username='%s'"%(f,s,d,st,p,n,cid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('staff.staff_managecourier'))


	if action=='inactive':
		q="update login set `status`='0' where username='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecourier'))

	if action=='active':
		q="update login set `status`='1' where username='%s'"%(cid)
		update(q)
		return redirect(url_for('staff.staff_managecourier'))
		

	if "courier" in request.form:
		f=request.form['fname']
		s=request.form['street']
		d=request.form['district']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s'"%(u)
		res=select(q)
		if res:
			flash('already')
   
		else:
			q="insert into login values('%s','%s','courier',1)"%(u,pa)
			insert(q)
			q="insert into courier values(null,'0','%s','%s','%s','%s','%s','%s','%s')"%(u,f,s,d,st,p,n)
			insert(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managecourier'))		

	return render_template('staff_managecourier.html',data=data)


@staff.route('/staff_managecategory',methods=['post','get'])	
def staff_managecategory():
	data={}
	q="select * from category"
	res=select(q)
	data['categoryview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='active':
		q="update category set status='1' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)
		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update category set category_name='%s', category_description='%s' where category_id='%s'"%(f,d,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
	if "category" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="select * from category where category_name='%s'"%(f)
		res=select(q)
		if res:
			flash("ALREADY ADDED")
		else:
		
  
  
			q="insert into category values(null,'%s','%s','1')"%(f,d)
			insert(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managecategory'))
		
	return render_template('staff_managecategory.html',data=data)

@staff.route('/staff_managesubcategory',methods=['post','get'])
def staff_managesubcategory():
	data={}
	q="select * from category where status='1'"
	res=select(q)
	data['categorydrop']=res
	q="select * from subcategory INNER JOIN category USING (`category_id`)"
	res=select(q)
	data['subview']=res
 

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update subcategory set sub_status='1' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managesubcategory'))

	if action=='inactive':
		q="update subcategory set sub_status='0' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managesubcategory'))

	if action=='update':
		q="select * from subcategory INNER JOIN category USING (`category_id`) where subcategory_id='%s'"%(sid)
		res=select(q)
		data['subcategoryupdate']=res


	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update subcategory set subcategory_name='%s',subcategory_description='%s' where subcategory_id='%s'"%(f,d,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managesubcategory'))

			
	if "subcategory" in request.form:
		cat=request.form['cat']
		f=request.form['fname']
		d=request.form['dis']
		q="select * from subcategory where subcategory_name='%s'"%(f)
		res=select(q)
		if res:
				flash("ALREADY ADDED")
		else:
      
				q="insert into subcategory values(null,'%s','%s','%s','1')"%(cat,f,d)
				insert(q)
				flash('successfully')
        
		return redirect(url_for('staff.staff_managesubcategory'))
	return render_template('staff_managesubcategory.html',data=data)

@staff.route('/staff_managecolor',methods=['post','get'])	
def staff_managecolor():
	data={}
	q="select * from color"
	res=select(q)
		
	data['colorview']=res


	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='active':
		q="update color set color_status='1' where color_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecolor'))

	if action=='inactive':
		q="update color set color_status='0' where color_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecolor'))

	if action=='update':
		q="select * from color where color_id='%s'"%(cid)
		res=select(q)
		data['colorupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update color set color_name='%s',color_desc='%s' where color_id='%s'"%(f,d,cid)
		update(q)
		return redirect(url_for('staff.staff_managecolor'))

	if "color" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="select * from color where color_name='%s'"%(f)
		res=select(q)
		if res:
				flash("ALREADY ADDED")
		else:
			q="insert into color values(null,'%s','%s','1')"%(f,d)
			insert(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managecolor'))
	return render_template('staff_managecolor.html',data=data)


@staff.route('/staff_managebrand',methods=['post','get'])	
def staff_managebrand():
	data={}
	q="select * from brand"
	res=select(q)
	data['brandview']=res

	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']

	else:
		action=None

	if action=='active':
		q="update brand set brand_status='1' where brand_id='%s'"%(bid)
		update(q)

		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

	if action=='inactive':
		q="update brand set brand_status='0' where brand_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

	if action=='update':
		q="select * from brand where brand_id='%s'"%(bid)
		res=select(q)
		data['brandupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update brand set brand_name='%s',brand_desc='%s' where brand_id='%s'"%(f,d,bid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))
								

	if "brand" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="select * from brand where brand_name='%s'"%(f)
		res=select(q)
		if res:
				flash("ALREADY ADDED")
		else:
			q="insert into brand values(null,'%s','%s','1')"%(f,d)
			insert(q)
			flash('added successfully')
			return redirect(url_for('staff.staff_managebrand'))
	return render_template('staff_managebrand.html',data=data)


@staff.route('/staff_manageitem',methods=['post','get'])	
def staff_manageitem():
	data={}

	

	q="select * from subcategory where sub_status='1'"
	res=select(q)
	data['subcategorydrop']=res

	q="select * from color where color_status='1' "
	res=select(q)
	data['colordrop']=res

	q="select * from brand where brand_status='1'"
	res=select(q)
	data['branddrop']=res


	q="SELECT * FROM product  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (`color_id`) INNER JOIN brand USING (brand_id)"
	res=select(q)
	data['productview']=res



	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']

	else:
		action=None

	if action=='available':
		q="update product set product_status='1' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_manageitem'))

	if action=='notavailable':
		q="update product set product_status='0' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_manageitem'))	

	if action=='update':
		q="SELECT * FROM product   INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (`color_id`) INNER JOIN brand USING (brand_id) where product_id='%s'"%(pid)
		res=select(q)
		
		data['productupdate']=res


	if "update" in request.form:
		
		sub=request.form['subcategory']
		col=request.form['color']
		b=request.form['brand']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/images"+str(uuid.uuid4())+i.filename
		i.save(path)
		
		
		q="update product set subcategory_id='%s',color_id='%s',brand_id='%s',product_name='%s',product_description='%s',product_image='%s' where product_id='%s'"%(sub,col,b,f,d,path,pid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_manageitem'))


	if "product" in request.form:
		
		sub=request.form['subcategory']
		col=request.form['color']
		b=request.form['brand']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/images"+str(uuid.uuid4())+i.filename
		i.save(path)
		exp=request.form['exp']
		
		q="select * from product where product_name='%s'"%(f)
		res=select(q)
		if res:
					flash("ALREADY ADDED")
		else:
        
			q="insert into product values(null,'%s','%s','%s','%s','%s','%s','%s','0','1')"%(sub,col,b,f,d,path,exp)
			insert(q)
			flash('successfully')
			return redirect(url_for('staff.staff_manageitem'))		
	return render_template('staff_manageitem.html',data=data)



@staff.route('/staff_managepurchase',methods=['post','get'])	
def staff_managepurchase():
	data={}

	q="select * from vendor where vendor_status='1'"
	res=select(q)
	data['vendordrop']=res


	q="select * from product where product_status='1'"
	res=select(q)
	data['productdrop']=res



	q="SELECT * FROM `purchase_child` INNER JOIN `purchase_master` USING (`purchase_master_id`) INNER JOIN `vendor` USING (`vendor_id`) INNER JOIN `product` USING (`product_id`) where status='pending'"
	res=select(q)
	data['purchaseview']=res


	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if  action=='conform':
		q="update purchase_master set status='purchased' where purchase_master_id='%s'"%(pid)
		update(q)

		q="select * from purchase_child where purchase_master_id='%s'"%(pid)
		res=select(q)

		for i in res:

			item_id=i['product_id']
			qty=i['quantity']
			q="update product set stock=stock+'%s' where product_id='%s'"%(qty,item_id)
			update(q)

			flash('successfully')

		return redirect(url_for('staff.staff_managepurchase'))
	if "purchase" in request.form:
		ve=request.form['ven']
		pro=request.form['pro']
		c=request.form['cost_price']
		qu=request.form['quantity']
		t=request.form['total']
		pid=request.form['pid']  
		sellp=(int(pro)/100)*int(c)
		new=int(sellp)+int(c)
		q="select * from purchase_master where vendor_id='%s' and status='pending'"%(ve)
		res=select(q)
		if res:
			pmid=res[0]['purchase_master_id']

		else:
			
			q="insert into purchase_master values(null,'%s','0','0','pending')"%(ve)
			pmid=insert(q)

		q="select * from purchase_child where product_id='%s' and purchase_master_id='%s' "%(pid,pmid)
		res=select(q)
		print(q)
		if res:

			pcid=res[0]['purchase_child_id']


			q="update purchase_child set quantity=quantity+'%s',cost_price=cost_price+'%s' where purchase_child_id='%s'"%(qu,c,pcid)
			update(q)
			print(q)

		else:


					
			q="insert into purchase_child values(null,'%s','%s','%s','%s','%s')"%(pmid,pid,c,new,qu)
			insert(q)
			print(q)

		q="update purchase_master set total=total+'%s' where purchase_master_id='%s'"%(t,pmid)
		update(q)
		flash('successfully')

		return redirect(url_for('staff.staff_managepurchase'))


		
	
	return render_template('staff_managepurchase.html',data=data)

@staff.route('/staff_viewbooking')
def staff_viewbooking():
	data={}
	q="SELECT * FROM `order_details`  INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
	res=select(q)
	data['bookingview']=res
	return render_template('staff_viewbooking.html',data=data)

@staff.route('/staff_viewpayment')
def staff_viewpayment():
	data={}
	oid=request.args['oid']
	q="SELECT * FROM `payment` INNER JOIN `card` USING (card_id) INNER JOIN `customer` USING (`customer_id`) INNER JOIN `order_master` USING (`order_master_id`) where order_master_id='%s'"%(oid)
	res=select(q)
	data['paymentview']=res
	return render_template('staff_viewpayment.html',data=data)	


@staff.route('/staff_viewpurchase')	
def staff_viewpurchase():
	data={}
	q="select * from purchase_child inner join product using (product_id) inner join purchase_master using (purchase_master_id)"
	res=select(q)
	data['purchaseview']=res
	return render_template('staff_viewpurchase.html',data=data)


@staff.route('/staff_sendreply',methods=['post','get'])
def staff_sendreply():

	
	if "reply" in request.form:
		rep=request.form['rep']
		cid=request.args['cid']
		q="update complaint set reply='%s' where complaint_id='%s'"%(rep,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewpurchase'))

	
	return render_template('staff_sendreply.html')	



@staff.route('/staff_viewcustomer')	
def staff_viewcustomer():
	data={}

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update login set status='1' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='1' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))

	if action=='reject':
		q="update login set status='0' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='0' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))
			
	q="select * from customer inner join login using (username)"
	res=select(q)
	data['customerview']=res

	return render_template('staff_viewcustomer.html',data=data)

@staff.route('/staff_managereport',methods=['post','get'])	
def staff_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['customer']	
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where (`customer_fname` like '%s') or (`date` like '%s'  ) or (`date` like '%s' ) "%(customer,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
		res=select(q)
		data['report']=res
	
	return render_template('staff_managereport.html',data=data)

@staff.route('/staff_salesreport')
def staff_salesreport():
		data={}
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
		res=select(q)
		data['r']=res
		
		
		return render_template('staff_salesreport.html',data=data)	



@staff.route('/purchase',methods=['get','post'])
def purchase():
    data={}
    q="select * from vendor"
    data['ven']=select(q)
    q="select * from product"
    data['pro']=select(q)
    if 'submit' in request.form:
        ven=request.form['vid']
        proid=request.form['pro']
        cprice=request.form['cprice']
        qty=request.form['qty']
        total=request.form['total']
        selling=request.form['selling']
        q="select * from purchase_master where pstatus='pending'"
        res=select(q)
        if res:
            pmmid=res[0]['pmaster_id']
            q="select * from purchase_details where pmaster_id='%s' and  product_id='%s'"%(pmmid,proid)
            resq=select(q)
            if resq:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="update purchase_details set quantity=quantity+'%s' where product_id='%s' and pmaster_id='%s'"%(qty,proid,pmmid)
                update(q)
            else:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(pmmid,proid,cprice,selling,qty)
                insert(q)
        else:
            q="insert into purchase_master values(null,'%s',0,'%s','pending',now())"%(ven,total)
            id=insert(q)
            q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(id,proid,cprice,selling,qty)
            insert(q)
            flash('Product Added to Purchase List...')
            return redirect(url_for('staff.staffmanagepurchase'))
    
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id and pstatus='pending'"
    res=select(q)
    data['res']=select(q)

    if 'btn' in request.form:
        q="update purchase_master set pstatus='paid' where pstatus='pending'"
        update(q)
        flash('Purchase Completed...')
        return redirect(url_for('staff.staffmanagepurchase'))
    return render_template('staff_manage_purchase.html',data=data)


@staff.route('/staffviewpur')
def staffviewpur():
    data={}
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id "
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_purchasedlist.html',data=data)


@staff.route('/admin_assign',methods=['get','post'])
def admin_assign():
    data={}
    q="select * from courier inner join login using(username) where status='1'"
    res=select(q)
    data['cou']=res
    
    
    if "update" in request.form:
        cou=request.form['cou']
        oid=request.args['oid']
        
        q="insert into delivery values(null,'%s','%s',curdate(),'Assign')"%(oid,cou)
        insert(q)
        return redirect(url_for('staff.staff_viewbooking'))
        
        
    return render_template('admin_assign.html',data=data)
    
@staff.route('/cusreport')
def cusreport():
	data={}
	q="select * from customer"
	data['custview']=select(q)

	return render_template('cusreport.html',data=data)	
@staff.route('/purchasereport')	
def purchasereport():
	data={}
	q="select * from purchase_child inner join product using (product_id)"
	res=select(q)
	data['purview']=res
	return render_template('purchasereport.html',data=data)
