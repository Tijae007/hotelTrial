from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.forms import CommentForm
from backend.forms import ReviewForm
from django.db.models import Count, Q
from .filters import HotelFilter

# Create your views here.
# def get_category_count():
#     queryset = Blog \
#         .objects \
#         .values('categories__') \
#         .annotate(Count('categories'))
#     return queryset

def index(request):
    news = Blog.objects.order_by('-date')[:4]
    # featured = Hotel.objects.filter(featured=True)[:4]
    # sponsored = Hotel.objects.filter(sponsored=True)[:4]
    latest = Hotel.objects.order_by('-date')[:4]
    featured = Hotel.objects.filter(featured=True)[:4]
    sponsored = Hotel.objects.filter(sponsored=True)[:4]
    agents = UserProfile.objects.all()

    context = {
        'latest': latest,
        'news': news,
        'featured': featured,
        'sponsored': sponsored, 
        'agents': agents
    }

    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save() 

    return render(request, 'frontend/index.html', context)

def homepage(request):
    news = Blog.objects.order_by('-date')[:4]
    # featured = Hotel.objects.filter(featured=True)[:4]
    # sponsored = Hotel.objects.filter(sponsored=True)[:4]
    latest = Hotel.objects.order_by('-date')[:4]
    featured = Hotel.objects.filter(featured=True)[:4]
    sponsored = Hotel.objects.filter(sponsored=True)[:4]
    agents = UserProfile.objects.all()

    context = {
        'latest': latest,
        'news': news,
        'featured': featured,
        'sponsored': sponsored, 
        'agents': agents
    }

    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save() 

    return render(request, 'frontend/homepage.html', context)

def about(request):
    about = About.objects.all()
    user_var = User.objects.order_by('-last_name')
    context = {'abt':about, 'user':user_var}
    return render(request, 'frontend/about.html', context)

def about_detail(request, abt_id):
    detail = About.objects.get(id=abt_id)
    return render(request, 'frontend/about_detail.html', {'det':detail})

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

    return render(request, 'frontend/blog.html', context)

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

    return render(request, 'frontend/hotels-grid-sidebar-2.html', context)


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
    return render(request, 'frontend/hotel-detail.html', {'pst':post, 'Rform':Rform, 'revs':reviews})

# def hotel_detail(request, all_id):
#     try:
#         post = Hotel.objects.get(id=all_id)
#     except ObjectDoesNotExist:
#         return render(request, 'frontend/404.html')
#     return render(request, 'frontend/hotel-detail.html', {'pst':post})


# def blog(request):
#     # category_count = get_category_count()
#     # print(category_count)
#     most_recent = Blog.objects.order_by('-date')[:4]
#     agents = UserProfile.objects.all()
#     blg_post = Blog.objects.order_by('-date')
#     paginator = Paginator(blg_post, 4)
#     page_request_var = 'page'
#     page = request.GET.get('page_request_var')
#     try:
#         paginated_queryset = paginator.page(page)
#     except PageNotAnInteger:
#         paginated_queryset = paginator.page(1)
#     except EmptyPage:
#         paginated_queryset = paginator.page(paginator.num_pages)
    
#     context = {
#         'queryset': paginated_queryset, 
#         'most_recent': most_recent,
#         'page_request_var': page_request_var, 
#         'agents': agents
#         # 'category_count': category_count 
#     }


#     return render(request, 'frontend/blog.html', context)

# def blog(request):
#     most_recent = Blog.objects.order_by('-date')[:4]
#     agents = UserProfile.objects.all()
#     blg_post = Blog.objects.order_by('-date')
#     paginated_filter = Paginator(blg_post, 3)
#     page_number = request.GET.get('page')
#     person_page_obj = paginated_filter.get_page(page_number)
#     context = {
#         'person_page_obj': blg_post, 
#         'most_recent': most_recent,
#         'agents': agents
#     }
#     context['person_page_obj'] = person_page_obj

#     return render(request, 'frontend/blog.html', context)

# def blog_post(request, blg_id):
#     most_recent = Blog.objects.order_by('-date')[:3]
#     form = CommentForm(request.POST or None)
#     if request.method == "POST": 
#         if form.is_valid():
#             form.save() 
#     single_post = {
#         'form': form,
#         'most_recent': most_recent
#     }
#     try:
#         single_post = Blog.objects.get(id=blg_id)
        
#     except ObjectDoesNotExist:
#         return render(request, 'frontend/404.html')
#     return render(request, 'frontend/blog-post.html', {'sipst':single_post})

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
            return redirect('frontend:blog_post', pk=single_post.pk)
        #  single_post = {'form': form, 'most_recent': most_recent,}
    else:
        form = CommentForm()
    return render(request, 'frontend/blog-post.html', {'comm':comments, 'form':form, 'sipst':single_post})

def help(request):
    return render(request, 'frontend/help.html')

def faq(request):
    
    return render(request, 'frontend/faq.html')

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

    return render(request, 'frontend/contacts.html')

def post_from_cat(request, category_id):
    count_post = Hotel.objects.filter(cat_id__id=category_id).count()
    try:
        get_cat_name = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    # get_cat_name = Category.objects.get(id=category_id)
    post_cat= Hotel.objects.filter(cat_id__id=category_id)
    context = {'posts': post_cat, 'counts': count_post, 'cat': get_cat_name}
    return render(request, 'frontend/post-cat.html', context)

def search(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(blg_title__icontains=query) |
            Q(blg_content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
        
    }
    return render(request, 'frontend/search_results.html', context)

def hotel_filter(request):
    filter = HotelFilter(request.GET, queryset=Hotel.objects.all())
    context = {}
        # 'filter': f
    
    context['filter'] = filter.qs
    return render(request, 'frontend/filter.html', context=context) 