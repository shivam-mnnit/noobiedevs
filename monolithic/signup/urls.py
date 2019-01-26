from sys import path

from django.conf.urls import include, url

from django.urls import path

from . import views

urlpatterns = [

    url(r'^$', views.signUP, name='signup'),
    url('MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^home/$', views.signin, name='signin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^welcome/$', views.home, name='home'),
    url(r'^home/MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^home/upload.html/$', views.upload, name='upload'),
    url(r'^welcome/MNNIT_KART.html/$', views.about, name='kart'),
    url(r'^welcome/upload.html/$', views.upload, name='upload'),
    url(r'^added/$', views.add, name='additem'),
    url(r'^dash/$', views.item_detail, name='collect'),
    url(r'^dash/upload.html/$', views.upload, name='dash_upload'),
    url(r'^delete_post/(?P<id>\d+)/$', views.delete_post, name='delete_post'),
    url('logout/$',views.signout,name='signout'),
    url('Male/$',views.Male,name='Male'),
    url('Male/upload.html',views.upload,name='upload'),
    url('Female/$',views.Female,name='Female'),
    url('Female/upload.html',views.upload,name='upload'),
    url('all/$',views.item_detail,name='all'),
    url('all/upload.html',views.upload,name='upload'),
    url(r'^find_image/$',views.new_page_vj,name='search_function'),
    url(r'^find_image/upload.html/$',views.upload,name='upload'),

    # url(r'^lost/$' ,views.lost, name='lost'),
]