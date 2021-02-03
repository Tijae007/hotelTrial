from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 


# Create your models here.
class UserProfile(models.Model):
    user_image = models.FileField(null=True, verbose_name='User Image', blank=True, upload_to='uploads/')
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
    
    def post_img(self):
        if self.user_image:
          return self.user_image.url


class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')
    
    def __str__(self):
        return self.cat_name
    
    class Meta():
        verbose_name_plural='Hotel Category'

class BlogCategory(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name=' Blog Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Blog Category Description')
    
    def __str__(self):
        return self.cat_name
    
    class Meta():
        verbose_name_plural='Blog Category'



class About(models.Model):
    pst_image = models.FileField(null=True, verbose_name='Founder Image', blank=True, upload_to='uploads/')
    pst_name = models.CharField(max_length=150, verbose_name= 'Founder Name')
    pst_title = models.CharField(max_length=150, verbose_name= 'Founder Title')

    content = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cat_id = models.ManyToManyField(Category, verbose_name='Category')
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pst_title
    
    def profile_img(self):
        if self.pst_image:
            return self.pst_image.url
        return '/static/frontend/img/avatar1.jpg'
    
    class Meta():
        verbose_name_plural = 'About'

class Hotel(models.Model):
    FEATURE = 'Feature'
    NO_FEATURE = 'No Feature'
    CHOOSE = ''
    APPEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (NO_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please Choose')
    ]
    pst_title = models.CharField(max_length=150, verbose_name= 'Hotel Name')
    pst_image = models.FileField(null=True, verbose_name='Hotel Image', blank=True, upload_to='uploads/')
    pst_image1 = models.FileField(null=True, verbose_name='Hotel Image 1', blank=True, upload_to='uploads/')
    pst_image2 = models.FileField(null=True, verbose_name='Hotel Image 2', blank=True, upload_to='uploads/')
    appear_home = models.CharField(max_length=50, choices=APPEAR_HOME_FIELD, default=CHOOSE)
    price = models.IntegerField(verbose_name= 'Room Price')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_id = models.ManyToManyField(Category, verbose_name='Category')
    date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    sponsored = models.BooleanField()

    def __str__(self):
        return self.pst_title
    
    class Meta():
        verbose_name_plural = 'Hotel'

    def post_img(self):
        if self.pst_image:
          return self.pst_image.url
    
    def post_img1(self):
        if self.pst_image1:
          return self.pst_image1.url
    
    def post_img2(self):
        if self.pst_image2:
          return self.pst_image2.url


class Blog(models.Model):
    FEATURE = 'Feature'
    NO_FEATURE = 'No Feature'
    CHOOSE = ''
    APPEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (NO_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please Choose')
    ]
    blg_title = models.CharField(max_length=150, verbose_name= 'Blog Title')
    blg_image = models.FileField(null=True, verbose_name='Blog Image', blank=True, upload_to='uploads/')
    appear_home = models.CharField(max_length=50, choices=APPEAR_HOME_FIELD, default=CHOOSE)
    blg_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_id = models.ManyToManyField(BlogCategory, verbose_name='Category')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blg_title
    
    class Meta():
        verbose_name_plural = 'Blog'

    def blog_img(self):
        if self.blg_image:
          return self.blg_image.url
    
    @property
    def get_comments(self):
        return self.comments.all()
    
  
class Comment(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(verbose_name= 'Content')
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
    



class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Review(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    CHOOSE = ''
    RATING_FIELD = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (CHOOSE, 'Choose Rating'),
    ]

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    rating = models.CharField(max_length=15, default=CHOOSE, choices=RATING_FIELD)
    email = models.EmailField(max_length=150, verbose_name= 'Email')
    timestamp = models.DateTimeField(auto_now_add=True)
    review_content = models.TextField(verbose_name= 'Your Review')
    post = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name





