from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# class CategoryForm(forms.ModelForm):
#     cat_name = forms.CharField()
#     cat_desc = forms.CharField(required=False, widget=forms.Textarea)

#     class Meta():
#         fields = '__all__'
#         model = Category

    

   
class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
                           widget=forms.Textarea(
                               attrs={'class': 'form-control'}
                           ))
    catch_bot = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field

    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name').capitalize()
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email*',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user


class BlogForm(forms.ModelForm):
    # FEATURE = 'Feature'
    # NO_FEATURE = 'No Feature'
    # CHOOSE = ''
    # APEAR_HOME_FIELD=[
    #     (FEATURE, 'Appear on home'),
    #     (NO_FEATURE, "Don't show on home"),
    #     (CHOOSE, 'Please Choose')
    # ]

    # pst_title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'placeholder': 'Post Title'})
    # )
    # appear_home = forms.CharField(
    #     widget=forms.Select(
    #         attrs={'class': 'form-control'}, choices=APEAR_HOME_FIELD)

    # )

    # content = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control'})
    # )
    # pst_image = forms.FileField(required=False)
    # cat_id = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    # catch_bot = forms.CharField(required=False,
    #                             widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        exclude = ['date', 'user']
        model = Blog

class EditUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))

    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    
    # description = forms.CharField(label='Description', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'About Yourself'}))

    # pst_image = forms.FileField(required=False)

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        # user.description = self.cleaned_data['description']
        # user.pst_image = self.cleaned_data['pst_image']
        if commit:
            user.save()
            return user

class PasswordChangeForm(PasswordChangeForm):
    # password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    
    # description = forms.CharField(label='Description', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'About Yourself'}))

    # pst_image = forms.FileField(required=False)

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        

        # user.description = self.cleaned_data['description']
        # user.pst_image = self.cleaned_data['pst_image']
        if commit:
            user.save()
            return user

# class EditUserForm(UserChangeForm):
#     class Meta():
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')

class EditBlog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ('blg_title', 'blg_image', 'blg_content')


class CommentForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        # fields = ('content', )

class ListingForm(forms.ModelForm):
    # listing_title = forms.CharField(label='Listing Title', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Listing Name'}))
    # category = forms.CharField(label='Category', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Listing Category'}))
    # keywords = forms.CharField(label='Keywords', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Keywords shoudld be seperated by commas'}))
    # # description = forms.CharField(label='Description', widget=forms.TextInput(
    # #     attrs={'class': 'form-control', 'placeholder': 'Description'}))
    # phone = forms.CharField(label='Phone*', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    # email = forms.CharField(label='Email*', widget=forms.EmailInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    # website = forms.CharField(label='Website*', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Website url'}))
    # city = forms.CharField(label='City', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter City'}))
    # address = forms.CharField(label='Address*', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'ex. 250, Fifth Avenue'}))
    # state = forms.CharField(label='State*', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter State'}))
    # # price = forms.CharField(label='Price*', widget=forms.TextInput(
    # #     attrs={'class': 'form-control', 'placeholder': 'Enter Price'}))
    
    # botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
    #                            validators=[validators.MaxLengthValidator(0)])

    # def clean_email(self):
    #     email_field = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email_field).exists():
    #         raise forms.ValidationError('Email already exist')
    #     return email_field

    class Meta():
        model = Hotel
        exclude = ['date', 'user']

        # fields = ['content', 'price', 'pst_title', 'pst_image', 'pst_image1', 'pst_image2', 'cat_id', 
        # 'appear_home', ]

# 'phone', 'email', 'website', 'city', 'state', 'address', 'keywords',
# 'listing_title', 'category',  'description', 
#          'price'
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     # user.listing_title = self.cleaned_data['listing_title']
    #     # user.category = self.cleaned_data['category']
    #     user.keywords = self.cleaned_data['keywords']
    #     # user.description = self.cleaned_data['description']
    #     user.phone = self.cleaned_data['phone']
    #     user.keywords = self.cleaned_data['keywords']
    #     user.email = self.cleaned_data['email']
    #     user.website = self.cleaned_data['website']
    #     user.city = self.cleaned_data['city']
    #     user.state = self.cleaned_data['state']
    #     user.address = self.cleaned_data['address']
    #     # user.price = self.cleaned_data['price']

    #     if commit:
    #         user.save()
    #         return user

class ReviewForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    review_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your review',
        'id': 'userreview',
        'rows': '4'
    }))
    class Meta:
        model = Review
        exclude = ['timestamp', 'post', 'email', 'review_content']
        # fields = ('content', )

# list of two tuples 