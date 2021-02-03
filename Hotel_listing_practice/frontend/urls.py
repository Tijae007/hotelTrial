from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('homepage-page/', views.homepage, name='homepage'),
    path('hotel-page/', views.hotel, name='hotel'),
    path('hotel-detail-page/<int:pk>', views.hotel_detail, name='hotel_detail'),
    path('detail-page/<int:abt_id>', views.about_detail, name='about_detail'),
    path('blog-page/', views.blog, name='blog'),
    path('blog-post-page/<int:pk>', views.blog_post, name='blog_post'),
    path('help-page/', views.help, name='help'),
    path('faq-page/', views.faq, name='faq'),
    path('contact-page/', views.contact, name='contact'),
    path('post-cat/<int:category_id>', views.post_from_cat, name='post_from_cat'),
    path('search-page/', views.search, name='search'),
    path('filter-page/', views.hotel_filter, name='hotel_filter'),

 
]
