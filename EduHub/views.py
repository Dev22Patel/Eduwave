from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users_app.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth import logout
from Course_app.models import *
from feedback.models import Review


def index(request):
    c=Review.objects.all()
    context={
        "images":c,
    }
    return render(request,'index.html',context)


def Mainpage(request):
    allevents = Course.objects.all()
    context={
        'course':allevents
    }
    c=Review.objects.all()
    context={
        "images":c,
    }
    return render(request , 'index.html', context)


@login_required
def home(request):
    user = request.user
    user_role = 'No role assigned'  # Default message if the user has no role
    c=Review.objects.all()

    try:
        user_profile = UserProfile.objects.get(user=user)
        user_role = user_profile.role
    except UserProfile.DoesNotExist:
        pass  # You can handle users without a profile differently if needed

    return render(request, 'home.html', {'username': user.username, 'user_role': user_role, 'images':c})

@login_required
def view_events(request):
    allevents = Course.objects.all()
    context={
        'course':allevents
    }
    return render(request,'show_events.html',context)

@login_required
def to_cart(request):
    context={
        'cart_items':CartItem.objects.filter()
    }
    return render(request,'cart.html',context)

def logout_view(request):
    logout(request)
    return redirect('index')



def view_profile(request):
    user_profile = request.user
    # Pass the user object to the template context
    context = {
        'user_profile': user_profile
    }
    
    # Render the template with the context
    return render(request, 'user_profile.html', context)


def orders(request):
    user = request.user
    course = Course.objects.all()
    orders = Cart.objects.filter(user=user, is_paid=True).prefetch_related('cart_items__course')

    context = {
        'orders': orders,
        'course': course,
    }
    return render(request, 'orders.html', context)


def success(request):
     payment_request = request.GET.get('payment_request_id')
     cart = Cart.objects.get(instamojo_id = payment_request)
     cart.is_paid = True
     cart.save()
     return redirect('/orders/')






