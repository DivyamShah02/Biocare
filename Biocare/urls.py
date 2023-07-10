from django.contrib import admin
from django.urls import path
from Biocare import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    # -- BACKEND --- #
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/favicon.ico'))),
    path('error/',views.error,name='error'),
    
    # -- ADMIN --- #
    path('admin/', admin.site.urls,name='admin'),
    
    # -- PAGES --- #    
    path('',views.home,name='home'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.contact_us,name='contact_us'),
    
    # -- BLOGS --- #
    path('blogs/',views.blogs,name='blogs'),
    path('blog/<str:slug>',views.blog_info,name='blog_info'),
    path('blog_add/',views.blog_add,name='blog_add'),
    
    # -- PRODUCTSS --- #    
    path('products/',views.products,name='products'),
    path('product/<str:slug>',views.product_info,name='product_info'),
    path('product_add/',views.product_add,name='product_add'),
    
    # -- ACCOUNTS --- #
    path('sign_in/',views.sign_in,name='sign_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('register/',views.register,name='register'),
    path('activation/<int:id>',views.activation,name='activation'),
    path('distributor_form/',views.distributor_form,name='distributor_form'),
    path('distributor_check/',views.distributor_check,name='distributor_check'),
    path('distributor_activate/<int:id>',views.distributor_activate,name='distributor_activate'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
