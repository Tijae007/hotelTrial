# from django.contrib.auth.models import User
import django_filters
from .models import Hotel, Category

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = ['price', 'cat_id']
    
        # model = Category
        # fields = ['cat_name']