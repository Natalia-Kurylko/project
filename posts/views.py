from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny,IsAuthenticated

from likes.models import Like
from posts.filter import LikeFilter
from .models import Post
from .serializers import PostSerializer, UserSerializer, UserActiveInfoSerializer,LikeSerializer
from likes.mixins import LikedMixin




User = get_user_model()

class PostViewSet(LikedMixin,viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserActiveViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserActiveInfoSerializer
    permission_classes = (IsAuthenticated,)


class LikeViews(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['created',]
    filter_class = LikeFilter


