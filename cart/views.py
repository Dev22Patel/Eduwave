from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
from Course_app.models import *;
from django.contrib import messages

api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN , endpoint="https://test.instamojo.com/api/1.1/")

from django.shortcuts import redirect
from django.contrib import messages

from django.contrib import messages

def add_cart(request, c_uid):
    user = request.user
    course_obj = Course.objects.get(uid=c_uid)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    # Check if the item is already in the cart
    if CartItem.objects.filter(cart=cart, course=course_obj).exists():
        messages.error(request, 'This item is already in your cart.')
    else:
        cart_item = CartItem.objects.create(
            cart=cart,
            course=course_obj
        )
        messages.success(request, 'Item added to your cart successfully.')

    return redirect('/viewevents/') 






@login_required(login_url='/login/')
def cart(request):
    try:
        cart = Cart.objects.get(is_paid=False, user=request.user)
    except Cart.DoesNotExist:
        cart = None

    if cart is None or cart.cart_items.count() == 0:
        # Handle the case where the cart is empty
        # For example, redirect to a page indicating that the cart is empty
        return render(request, 'empty_cart.html')

    response = api.payment_request_create(
        amount=cart.get_cart_total(),
        purpose='Buying Course',
        buyer_name=request.user.username,
        email="notrealdev2211@gmail.com",
        redirect_url='http://127.0.0.1:8000/success/',
    )
    cart.instamojo_id = response['payment_request']['id']
    cart.save()
    context = {'cart': cart, 'payment_url': response['payment_request']['longurl']}
    print(response)
    return render(request, 'cart.html', context)



def delete_item(request,cart_item_uid):
     CartItem.objects.get(uid = cart_item_uid).delete()
     return redirect('/to_cart/cart/')