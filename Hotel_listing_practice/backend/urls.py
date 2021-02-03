from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('user-login-page/', views.login_userview, name='login_userview'),
   path('dashboard-page/', views.dashboard, name='dashboard'),
   path('user_dashboard-page/', views.user_dashboard, name='user_dashboard'),
   path('logout_view-page/', views.logout_view, name='logout_view'),
   path('messages-page/', views.messages, name='messages'),
   path('bookings-page/', views.bookings, name='bookings'),
   path('listings-page/', views.listings, name='listings'),
   path('listings2-page/', views.listings2, name='listings2'),
   path('reviews-page/', views.reviews, name='reviews'),
   path('add-listing-page/', views.add_listing, name='add_listing'),
   path('user-profile-page/', views.user_profile, name='user_profile'),
   path('charts-page/', views.charts, name='charts'),
   path('tables-page/', views.tables, name='tables'),
   path('register-page/', views.register_form, name='register_form'),
   path('pass-form-page/', views.pass_form, name='pass_form'),
   path('edit-form-page/', views.edit_form, name='edit_form'),
   path('reset/', views.reset, name='reset'),
   path('blog-form/', views.blog_form, name='blog_form'),
   path('show-post/', views.show_post, name='show_post'),
   path('show-post2/', views.show_post2, name='show_post2'),
   path('edit-blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
   path('delete-post/<int:blog_id>', views.delete_post, name='delete_post'),
   path('delete-hotel/<int:listf_id>', views.delete_hotel, name='delete_hotel'),
   path('view-blog/<int:pk>', views.view_blogdetails, name='view_blogdetails'),
   path('view-listing/<int:pk>', views.view_listingdetails, name='view_listingdetails'),
   path('about-page/', views.about, name='about'),
   path('detail-page/<int:abt_id>', views.about_detail, name='about_detail'),
   path('hotel-page/', views.hotel, name='hotel'),
   path('hotel-detail-page/<int:pk>', views.hotel_detail, name='hotel_detail'),
   path('blog-page/', views.blog, name='blog'),
   path('blog-post-page/<int:pk>', views.blog_post, name='blog_post'),
   path('contact-page/', views.contact, name='contact'),




#    path('show-listing/', views.show_listing, name='show_listing'),










    
]
