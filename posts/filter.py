
from django_filters import rest_framework as filters
from posts.models import Like




class LikeFilter(filters.FilterSet):

    date_from= filters.DateFilter(field_name="created",lookup_expr="gt")
    date_to= filters.DateFilter(field_name="created",lookup_expr='lt')
    class Meta:
        model = Like
        fields = ('created',)
