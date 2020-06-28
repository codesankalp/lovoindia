from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect

# Create your views here.
import json
from django.contrib.auth.decorators import login_required
from .models import Seller,Product,Subscribe,ImageUploadForm


# ... index definition ...


def home(request):
    all_product = Product.objects.all()
    context = {
        "product":all_product[:4]
    }
    return render(request, "pages/index.html",context)


@login_required
def profile(request):
    try:
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        userdata = {
            'user_id': auth0user.uid,
            'name': user.first_name,
            'picture': auth0user.extra_data['picture']
        }

        try:
            seller = Seller.objects.get(username=user.username)
            value = 1
        except:
            seller = {}
            value = 0

        return render(request, 'pages/profile.html', {
            'auth0User': auth0user,
            'userdata': json.dumps(userdata, indent=4),
            'seller': seller,
            'value': value
        })
    except:
        return redirect(logout)


# ... index, profile ...

def logout(request):
    django_logout(request)
    domain = 'codesankalp.us.auth0.com'
    client_id = "LuQrbCXbnXEw4UcZFCWodhosFp2nBvb5"
    return_to = 'http://127.0.0.1:8000'
    return redirect(f"https://{domain}/v2/logout?client_id={client_id}")
    # return HttpResponseRedirect(f"https://{domain}/v2/logout?returnTo={return_to}")
    # return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')


@login_required
def register(request):
    user = request.user
    if request.method == 'GET':
        try:
            seller = Seller.objects.get(username=user.username)
            value = 1
        except:
            seller = {}
            value = 0

        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        context = {
            'auth0User': auth0user,
            'value':value,
            'seller': seller,
        }
        return render(request, "pages/registration.html", context=context)
    else:
        em = Seller()
        em.name = request.POST.get('name')
        em.username = request.POST.get('username')
        em.email = request.POST.get('email')
        em.set_password(request.POST.get('password'))
        em.address = request.POST.get('address')
        em.brand = request.POST.get('brand')
        em.phone = request.POST.get('phone')
        try:
            em.save()
        except:
            msg = "SOME DATA IS INCORRECT, GO BACK AND RETRY"
            return render(request,'pages/error.html',{'msg':msg})
        return redirect(home)

@login_required
def product_register(request):
    user = request.user
    if request.method == 'GET':
        try:
            seller = Seller.objects.get(username=user.username)
        except:
            seller = {}
        user = request.user
        auth0user = user.social_auth.get(provider='auth0')
        context = {
            'auth0User': auth0user,
            'seller': seller,
        }
        return render(request, "pages/product_reg.html", context=context)

    else:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.description = request.POST.get('description')
            # print(request.FILES['image'])
            product.image = form.cleaned_data['image']
            # product.image = request.POST.get(request.FILES['image'])
            product.category = request.POST.get('category')
            try:
                product.seller = Seller.objects.get(username=user.username)
            except:
                product.seller = {}
            try:
                product.save()
            except:
                msg = "SOME DATA IS INCORRECT, GO BACK AND RETRY"
                return render(request,'pages/error.html',{'msg':msg})
        return redirect('profile')
        
            

        



def subscribe(request):
    if request.method == "POST":
        sub = Subscribe()
        sub.email = request.POST.get("email")
        sub.save()
        msg = "Thanks For subscribing,we will reach to you shortly."
        return render(request,"pages/error.html",{"msg":msg})


def contact(request):
    return render(request, "pages/contact.html")


def shop(request):
    all_product = Product.objects.all()
    context = {
        "product":all_product
    }
    return render(request, "pages/shop_detail.html" ,context)


def cart(request):
    return render(request, "pages/shopping_cart.html")


def grid(request):
    all_product = Product.objects.all()
    context = {
        "product":all_product
    }
    return render(request, "pages/shop_grid.html",context)


def blog_details(request):
    return render(request, "pages/blog_detail.html")
