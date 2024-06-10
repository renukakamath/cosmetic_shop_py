from flask import *
from database import*
public=Blueprint('public',__name__)
@public.route('/')
def public_home():
	return render_template('public_home.html')
@public.route('/about')
def about():
    return render_template('about.html')
@public.route('/public_login',methods=['post','get'])
def public_login():
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		res=select(q)
		if res:
			session['username']=res[0]['username']
			lid=session['username']

			if res[0]['user_type']=="admin":
				return redirect(url_for('admin.admin_home'))
			elif res[0]['user_type']=="customer":
				q="select * from customer inner join login using (username) where username='%s' and status='0'"%(u)
				res=select(q)
				if res:
					flash('inactive')
				else:


					q="select * from customer where username='%s'"%(lid)
					res=select(q)
					if res:
						session['customer_id']=res[0]['customer_id']
						cid=session['customer_id']
						session['customer_fname']=res[0]['customer_fname']
						customer_fname=session['customer_fname']
					return redirect(url_for('customer.customer_home'))
			elif res[0]['user_type']=="staff":
				q="select * from staff inner join login using (username) where username='%s' and status='0'"%(u)
				res=select(q)
				if res:
					flash('inactive')
				else:
					q="select * from staff where username='%s'"%(lid)
					res=select(q)
					if res:
						session['staff_id']=res[0]['staff_id']
						sid=session['staff_id']
					return redirect(url_for('staff.staff_home'))

			elif res[0]['user_type']=="courier":
				q="select * from courier inner join login using (username) where username='%s' and status='0'"%(lid)
				res=select(q)
				if res:
					flash('inactive')
				else:
					q="select * from courier where username='%s'"%(lid)
					res=select(q)
					if res:
						session['courier_id']=res[0]['courier_id']
						cid=session['courier_id']
					
					return redirect(url_for('courier.courier_home'))


			elif res[0]['user_type']=="vendor":
				q="select * from vendor inner join login using (username) where username='%s' and status='0'"%(lid)
				res=select(q)
				if res:
					flash('inactive')
				else:
					q="select * from vendor where username='%s'"%(lid)
					res=select(q)
					if res:
						session['vendor_id']=res[0]['vendor_id']
						vid=session['vendor_id']
					
					return redirect(url_for('vendor.vendorhome'))

		else:
			flash('invalid username and password')
	
	return render_template('public_login.html')


@public.route('/customer_registration',methods=['post','get'])	
def customer_registration():
	if "cusreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		st=request.form['state']
		pi=request.form['pin']
		d=request.form['date']
		g=request.form['gen']
		n=request.form['num']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s'"%(u)
		res=select(q)
		if res:

			flash('already exist')

		else:
			
			q="insert into login values('%s','%s','customer','1')"%(u,pa)
			insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(u,f,l,h,s,di,st,pi,d,g,n)
			insert(q)
			print(q)
			flash('successfully')
			return redirect(url_for('public.public_login'))

	return render_template('customer_registration.html')

		

