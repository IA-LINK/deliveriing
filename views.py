from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



def home(request):
	orders = Order.objects.all()
	customer = Customer.objects.all()
	total_orders= orders.count()
	pending = orders.filter(status='Pending').count()
	delivered = orders.filter(status = 'Delivered').count()
	context = {'total_order': total_orders, 'pending': pending, 'Delivered':delivered, 'customer':customer,
	'orders':orders,

	 }


	return render(request, 'accounts/dashboard.html', context)




def productview(request):
	products = Product.objects.all()
	return render(request, 'accounts/product.html',{'products':products})




def customer(request, pk):
	customers = Customer.objects.get(id=pk)
	orders = customers.order_set.all()
	count_order = orders.count()
	context = { 'customers':customer, 'orders':orders, 'count_order':count_order }
	return render(request, 'accounts/customer.html', context)