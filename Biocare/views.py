from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
import random,datetime,json
from PIL import Image
from biocare_data.models import Product,Blog,Distributor
from Biocare.mail import SendMail

# --- BACKEND --- #
def error(request):
    return render(request,'404.html')

# --- PAGES --- #
def home(request):
    logged_in = request.GET.get('logged_in')
    if logged_in == 'true':
        success = 1
    else:
        success = 0   
    # print(str(request.user.is_authenticated)) 
    all_blog_data = Blog.objects.all()
    all_blog_data = list(reversed(all_blog_data))
    data = {
        'all_blog_data':all_blog_data[0:3],
        'success':success,
        'is_logged_in':request.user.is_authenticated,
    }
    return render(request,'index.html',data)

def contact_us(request):
    data = {
        'is_logged_in':request.user.is_authenticated,        
    }
    return render(request,'contact.html',data)

def about_us(request):
    data={
        'is_logged_in':request.user.is_authenticated,        
    }
    return render(request,'about_us.html',data)

# --- ACCOUNTS --- #
def sign_in(request):
    error = 0 # No error
    email = None # For validation in html
    try :
        if request.method == 'POST':
            # Storing data in variables
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_info = User.objects.filter(email=email) # Checking user in database
            if len(user_info) > 0:
                # User data is available
                if user_info[0].is_active == True:
                    username = user_info[0] # It is an object that stores user id
                    user = authenticate(request, username=username, password=password) # Authenticating user
                    if user is not None:
                        # User is authenticated
                        login(request, user)
                        request.session.set_expiry(30 * 24 * 60 * 60) # Storing user data in session (remembering the user)
                        url = 'https://www.biocareworld.com/?logged_in=true'
                        return redirect(url)
                    else:
                        error = 2 # Wrong password
                else:
                    domain = "https://www.biocareworld.com"
                    activate_url = reverse('activation', args=[user_info[0].username])
                    url = f"{domain}{activate_url}"
                    send_mail = SendMail()
                    send_mail.send_activation(link=url,email=email)
                    error = 4 # Not activated
            else:
                error = 1 # Not Register
    except:
        error = 3 # Fatal error
    data = {
        'error':error,
        'email':email,
        'is_logged_in':request.user.is_authenticated,        
    }
    return render(request,'sign_in.html',data)

def register(request):
    error = 0 #No Error
    if request.method=="POST":
            # Storing details in variables
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')            
            user_info = User.objects.filter(email=email) #Collecting Information
            if len(user_info) == 0:
                # User is not registered
                new_id = True
                # This loop is for generating unique User Id
                while new_id:
                # It checks user id is already used if yes than generates new id
                    uid = random.randint(1111111111,9999999999)
                    if len(User.objects.filter(username = uid)) == 0:
                        new_id = False
                # Creating new user
                user = User.objects.create_user(username=uid,email=email,password=password)
                user.first_name = first_name # Saving firstname
                user.last_name = last_name # Saving last name
                user.is_active = False
                user.save()                  
                domain = "https://www.biocareworld.com"
                activate_url = reverse('activation', args=[uid])
                url = f"{domain}{activate_url}"
                send_mail = SendMail()
                send_active_mail = send_mail.send_activation(link=url,email=email)                
                error = 2
            else:
                # User is already registered
                error = 1

    data = {
        'error':error,
        'is_logged_in':request.user.is_authenticated,        
    }
    return render(request, "register.html",data)

def activation(request,id):
    try:
        user_acc = User.objects.get(username = id)
        user_acc.is_active = True
        user_acc.save()
        url = 'https://www.biocareworld.com/?logged_in=true'
        # Logging user
        # user = authenticate(request, username=uid, password=password)
        login(request,user_acc)
        request.session.set_expiry(30 * 24 * 60 * 60) # Storing user data in session (remembering the user)                

        return redirect(url)
    
    except:
        return redirect('home')

def log_out(request):
    logout(request)
    return redirect('home') 

def distributor_form(request):
    error = 0
    user = request.user
    if request.method == 'POST':    
        if request.user.is_authenticated:
            if user.is_active:
                user_mail = request.POST.get('email')
                user_already = Distributor.objects.filter(user_mail=user_mail)
                if len(user_already) == 0:                    
                    user_id = user
                    new_distributor = Distributor(
                        user_id = user_id,
                        first_name = request.POST.get('first_name'),
                        last_name = request.POST.get('last_name'),
                        user_mail = user_mail,
                        user_number = request.POST.get('number'),
                        user_address = request.POST.get('address'),
                        user_pin_code = request.POST.get('pin_code'),
                        user_city = request.POST.get('city'),
                        user_state = request.POST.get('state'),
                        user_country = request.POST.get('country'),
                        delivery_mail = request.POST.get('co_email'),
                        company_name = request.POST.get('company'),
                        delivery_pin_code = request.POST.get('co_pin_code'),
                        delivery_city = request.POST.get('co_city'),
                        delivery_address = request.POST.get('co_address'),
                        delivery_state = request.POST.get('co_state'),
                        delivery_country = request.POST.get('co_country'),
                    )
                    new_distributor.save()
                    send_mail = SendMail()
                    send_mail.send_distributor_inprocess(email=new_distributor.user_mail,name=f'{new_distributor.first_name} {new_distributor.last_name}')
                    error = 5 # Profile created successfully
                else:
                    if user_already[0].accepted:
                        error = 3 # Distributor already exist
                    else:
                        error = 4 # Distributor yet to be checked
            else:
                error = 2 # Not activated
        else:
            error = 1 # Not logged in
    
    is_distributor = False
    distributor_accepted = False
    try:
        user_obj = Distributor.objects.filter(user_mail=user.email)
        is_distributor = True
        if len(user_obj)>0:
            distributor_accepted = user_obj[0].accepted
    except:
        is_distributor = False
        distributor_accepted = False
        pass
    data = {
        'is_logged_in':request.user.is_authenticated,     
        'error':error,   
        'user':request.user,
        'is_distributor':is_distributor,
        'distributor_accepted':distributor_accepted,
    }
    return render(request,'distributor_form.html',data)

@login_required(login_url=reverse_lazy('sign_in'))          
def distributor_check(request):
    user = request.user
    if user.is_staff:
        pass
    else:
        return redirect('home')
    distributor = Distributor.objects.filter(accepted=False)
    data={
        'distributor':distributor,
    }
    return render(request,'distributor_check.html',data)
 
@login_required(login_url=reverse_lazy('sign_in'))
def distributor_activate(request,id):
    user = request.user
    if user.is_staff:
        pass
    else:
        return redirect('home')
    distributor = Distributor.objects.get(user_id=id)  
    if distributor.accepted:
        return HttpResponse(f'<h2>Distributor {distributor.first_name} - {distributor.user_id} is already activated</h2>')
    else: 
        distributor.accepted = True
        distributor.save()
        send_mail = SendMail()
        send_mail.send_distributor_activated(email=distributor.user_mail,name=f'{distributor.first_name} {distributor.last_name}')
        return HttpResponse(f'<h2>Distributor {distributor.first_name} - {distributor.user_id} Activated</h2>')

# --- PRODUCTS --- #
def products(request):
    all_product_data = Product.objects.all()
    data = {
        'all_product_data':all_product_data,
        'is_logged_in':request.user.is_authenticated,        
    }
    
    return render(request,'products.html',data)

def product_info(request,slug):
    product_data = Product.objects.filter(slug=slug)
    if len(product_data) == 0:
        return redirect('products')
    similar_product_data = Product.objects.filter(category = product_data[0].category)
    similar_product_data = list(reversed(similar_product_data))
    data = {
        'product_data':product_data[0],
        'similar_product_data':similar_product_data[0:4],
        'is_logged_in':request.user.is_authenticated,
        
    }
    return render(request,'product_info.html',data)

@login_required(login_url=reverse_lazy('sign_in'))
def product_add(request):
    user = request.user
    if user.is_staff:
        pass
    else:
        return redirect('home')
    if request.method == 'POST':
        try:
            product_obj = Product(title=request.POST.get('title'),
                                  category=request.POST.get('category'),                                
                                  price_qty_1=request.POST.get('price_qty_1'),
                                  price_1=request.POST.get('price_1'),
                                  price_qty_2=request.POST.get('price_qty_2'),
                                  price_2=request.POST.get('price_2'),
                                  price_qty_3=request.POST.get('price_qty_3'),
                                  price_3=request.POST.get('price_3'),
                                  info=request.POST.get('info'),
                                  shop_link=request.POST.get('shop_link'),
                                  image=request.FILES.get('image'))
            for i in range(1,11):
                if request.POST.get(f'pt{i}_head') != '':                              
                    if i == 1:
                        product_obj.pt1_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt1_value = request.POST.get(f'pt{i}_value')
                    elif i == 2:
                        product_obj.pt2_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt2_value = request.POST.get(f'pt{i}_value')
                    elif i == 3:
                        product_obj.pt3_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt3_value = request.POST.get(f'pt{i}_value')
                    elif i == 4:
                        product_obj.pt4_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt4_value = request.POST.get(f'pt{i}_value')
                    elif i == 5:
                        product_obj.pt5_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt5_value = request.POST.get(f'pt{i}_value')
                    elif i == 6:
                        product_obj.pt6_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt6_value = request.POST.get(f'pt{i}_value')
                    elif i == 7:
                        product_obj.pt7_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt7_value = request.POST.get(f'pt{i}_value')
                    elif i == 8:
                        product_obj.pt8_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt8_value = request.POST.get(f'pt{i}_value')
                    elif i == 9:
                        product_obj.pt9_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt9_value = request.POST.get(f'pt{i}_value')
                    elif i == 10:
                        product_obj.pt10_head = request.POST.get(f'pt{i}_head')
                        product_obj.pt10_value = request.POST.get(f'pt{i}_value')
                        
            product_obj.save()
            return redirect(f'https://www.biocareworld.com/product/{product_obj.slug}')
        except Exception as e:
            return HttpResponse(f'{e}')
              
    return render(request,'product_add.html')
   
# --- BLOGS --- # 
def blogs(request):
    all_blog_data = Blog.objects.all()
    data = {
        'all_blog_data':all_blog_data,
        'is_logged_in':request.user.is_authenticated,
    }
    return render(request,'blogs.html',data)    

def blog_info(request,slug):
    blog_data = Blog.objects.filter(slug=slug)
    if len(blog_data) == 0:
        return redirect('blogs')
    siilar_blog_data = Blog.objects.filter(category = blog_data[0].category)
    siilar_blog_data = list(reversed(siilar_blog_data))
    latest_blog_data = Blog.objects.all()
    latest_blog_data = list(reversed(latest_blog_data))
    data = {
        'blog_data':blog_data[0],
        'similar_blog_data':siilar_blog_data[0:4],
        'blog_tags' : str(blog_data[0].tags).split(','),     
        'latest_blog_data':latest_blog_data[0:3],   
        'is_logged_in':request.user.is_authenticated,        
    }
    return render(request,'blog_info.html',data)

@login_required(login_url=reverse_lazy('sign_in'))
def blog_add(request):
    user = request.user
    if user.is_staff:
        pass
    else:
        return redirect('home')
    if request.method == 'POST':
        try:
            date=str(request.POST.get('date')).split('-')
            date = datetime.date(year=int(date[0]),month=int(date[1]),day=int(date[2]))
            
            blog_obj = Blog(title=request.POST.get('title'),
                                date=date,
                                category=request.POST.get('category'),                                                                                        
                                tags=request.POST.get('tags'),
                                para_1=request.POST.get('para_1'),
                                para_2=request.POST.get('para_2'),
                                head_image=request.FILES.get('head_image'),
                                secondary_image_1=request.FILES.get('secondary_image_1'),
                                secondary_image_2=request.FILES.get('secondary_image_2'),
                            )                                       
            blog_obj.save()
        except Exception as e:
            return HttpResponse(f'{e}')
              
    return render(request,'blog_add.html')
