from django.contrib.auth import get_user_model
from rest_framework import serializers

from likes.models import Like
from .models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'body', 'total_likes')


class UserActiveInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login')


class LikeSerializer(serializers.ModelSerializer):
    created = serializers.DateField

    class Meta:
        model = Like
        fields = ('created',)
