import django_filters
from .models import *

class SaleFilter(django_filters.FilterSet):
    class Meta:
        model = Sale
        fields = ('owner','customer','product',)


