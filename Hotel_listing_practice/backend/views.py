from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 

from django.contrib import messages

from frontend.models import *
from backend.forms import *

from django.contrib.auth import update_session_auth_hash

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.forms import CommentForm
from backend.forms import ReviewForm
from django.db.models import Count, Q
from frontend.filters import HotelFilter

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontend:homepage')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login2.html')

def login_userview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/userlogin.html')

@login_required(login_url='/dashboard/')
def dashboard(request):
    return render(request, 'backend/index.html')

@login_required(login_url='/user_dashboard/')
def user_dashboard(request):
    return render(request, 'backend/userindex.html')

@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')

@login_required(login_url='/dashboard/')
def messages(request):
    return render(request, 'backend/messages.html')

@login_required(login_url='/dashboard/')
def bookings(request):
    return render(request, 'backend/bookings.html')

@login_required(login_url='/dashboard/')
def listings(request):
    # hotel_list = Hotel.objects.order_by('-date')
    hotel_list = Hotel.objects.filter(user=request.user)
    return render(request, 'backend/listings.html', {'hlist':hotel_list})

@login_required(login_url='/dashboard/')
def new_listings(request):
    # hotel_list = Hotel.objects.order_by('-date')
    hotel_list = Hotel.objects.filter(user=request.user)
    return render(request, 'backend/newlistings.html', {'hlist':hotel_list})

def new_listings2(request):
    hotel_list = Hotel.objects.order_by('-date')
    # hotel_list = Hotel.objects.filter(user=request.user)
    return render(request, 'backend/newlistings.html', {'hlist':hotel_list})

def listings2(request):
    hotel_list = Hotel.objects.order_by('-date')
    # hotel_list = Hotel.objects.filter(user=request.user)
    return render(request, 'backend/listings.html', {'hlist':hotel_list})

@login_required(login_url='/dashboard/')
def reviews(request):
    review_list = Review.objects.filter(user=request.user)
    return render(request, 'backend/reviews.html', {'rlist':review_list})


@login_required(login_url='/dashboard/')
def add_listing(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            # messages.success(request, 'Hotel Posted')
            
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-listing.html', {'listf': list_form})

@login_required(login_url='/dashboard/')
def add_newlisting(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            # messages.success(request, 'Hotel Posted')
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-newlisting.html', {'listf': list_form})


@login_required(login_url='/dashboard/')
def user_profile(request):
    agents = UserProfile.objects.filter(user=request.user)
    return render(request, 'backend/user-profile.html', {'profile':request.user, 'agents': agents})

@login_required(login_url='/dashboard/')
def user_newprofile(request):
    agents = UserProfile.objects.filter(user=request.user)
    return render(request, 'backend/user-newprofile.html', {'profile':request.user, 'agents': agents})

@login_required(login_url='/dashboard/')
def charts(request):
    return render(request, 'backend/charts.html')

@login_required(login_url='/dashboard/')
def newcharts(request):
    return render(request, 'backend/newcharts.html')

def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # messages.success(request, 'User Registered')
    else:
        register_form = RegisterForm()
    return render(request, 'frontend/register.html', {'reg': register_form})

def pass_form(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/pass-form.html', {'pass_key':pass_form})

def pass_newform(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/pass-newform.html', {'pass_key':pass_form})

def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit-user-profile.html', {'edit_key':edit_form})

def edit_newform(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit-newuser-profile.html', {'edit_key':edit_form})

def reset(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/reset.html', {'pass_key':pass_form})

def blog_form(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()
            # messages.success(request, 'Blog Posted')
    else:
        blog_form = BlogForm()
    return render(request, 'backend/add-blog.html', {'blog': blog_form})

def edit_blog(request, blog_id):
    if request.method == 'POST':
        edit_form = EditBlog(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditBlog(instance=request.user)
    return render(request, 'backend/edit-user-profile.html', {'edit_key':edit_form})

def show_post(request):
    # list_blog = Blog.objects.order_by('-date')
    list_blog = Blog.objects.filter(user=request.user)
    return render(request, 'backend/view-blog.html', {'list':list_blog})

def show_post2(request):
    list_blog = Blog.objects.order_by('-date')
    # list_blog = Blog.objects.filter(user=request.user)
    return render(request, 'backend/view-blog.html', {'list':list_blog})

def delete_post(request, blog_id):
    post_record = get_object_or_404(Blog, id=blog_id)
    post_record.delete()
    return redirect('backend:show_post')

def delete_hotel(request, listf_id):
    post_record = get_object_or_404(Hotel, id=listf_id)
    post_record.delete()
    return redirect('backend:new_listings')

def delete_newhotel(request, listf_id):
    post_record = get_object_or_404(Hotel, id=listf_id)
    post_record.delete()
    return redirect('backend:listings')

def view_listingdetails(request, pk):
    post = get_object_or_404(Hotel, pk=pk)
    return render(request, 'backend/view-listing.html', {'pst':post})

def view_newlistingdetails(request, pk):
    post = get_object_or_404(Hotel, pk=pk)
    return render(request, 'backend/view-newlisting.html', {'pst':post})

def view_blogdetails(request, pk):
    single_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'backend/view-blogdetail.html', {'sipst':single_post})

def about(request):
    about = About.objects.all()
    user_var = User.objects.order_by('-last_name')
    context = {'abt':about, 'user':user_var}
    return render(request, 'backend/about.html', context)

def about_detail(request, abt_id):
    detail = About.objects.get(id=abt_id)
    return render(request, 'backend/about_detail.html', {'det':detail})

def hotel(request):
    most_recent = Hotel.objects.order_by('-date')[:4]
    all_post = Hotel.objects.order_by('-date')
    paginated_filter = Paginator(all_post, 4)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    context = {
        'person_page_obj': all_post, 
        'most_recent': most_recent,
    }
    context['person_page_obj'] = person_page_obj

    return render(request, 'backend/hotels-grid-sidebar-2.html', context)


def hotel_detail(request, pk):
    post = get_object_or_404(Hotel, pk=pk)
    reviews = Review.objects.filter(post=pk)
    if request.method == "POST":
        Rform = ReviewForm(request.POST)
        if Rform.is_valid():
            review = Rform.save(commit=False) 
            review.post = post
            review.save()
            return redirect('frontend:hotel_detail', pk=post.pk)
    else:
        Rform = ReviewForm()
    return render(request, 'backend/hotel-detail.html', {'pst':post, 'Rform':Rform, 'revs':reviews})

def blog(request):
    most_recent = Blog.objects.order_by('-date')[:4]
    agents = UserProfile.objects.all()
    blg_post = Blog.objects.order_by('-date')
    paginated_filter = Paginator(blg_post, 3)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    context = {
        'person_page_obj': blg_post, 
        'most_recent': most_recent,
        'agents': agents
    }
    context['person_page_obj'] = person_page_obj

    return render(request, 'backend/blog.html', context)

def blog_post(request, pk):
    # single_post = Blog.objects.get(pk=pk)
    single_post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('backend:blog_post', pk=single_post.pk)
        #  single_post = {'form': form, 'most_recent': most_recent,}
    else:
        form = CommentForm()
    return render(request, 'backend/blog-post.html', {'comm':comments, 'form':form, 'sipst':single_post})

def contact(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Contact Us Information'
        context = {
            'name':name,
            'lastname':lastname,
            'phone':phone,
            'email':email,
            'message': message
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <tijaniyunus07@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                    'teezee132@gmail.com', 'tijaniyunus07@gmail.com', email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'backend/contacts.html')
