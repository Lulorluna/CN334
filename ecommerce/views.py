from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ecommerce.models import *

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6610742410 Thanasak Chonreungchay views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)

def customer_all_view(request):
    customers = list(Customer.objects.all().values())
    return JsonResponse(customers, safe=False)

def customer_view(request, username):
    customer = list(Customer.objects.filter(user__username = username).values('user__username', 'user__email', 'address', 'province', 'post_code', 'tel'))
    return JsonResponse(customer, safe=False)

def product_all_view(request):
    products = list(Product.objects.all().values())
    return JsonResponse(products, safe=False)

def product_by_id_view(request, id):
    product = list(Product.objects.filter(id = id).values())
    return JsonResponse(product, safe=False)

def order_by_product_id_view(request, id):
    order = list(Order.objects.filter(productorder__product_id=id).values())
    return JsonResponse(order, safe=False)

def summarize_view(request):
    summary = ProductOrder.objects.values('product__name').annotate(
        total_quantity=models.Sum('quantity'),
        total_price=models.Sum('total_price')
    )
    return JsonResponse(list(summary), safe=False)


