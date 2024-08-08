from rest_framework import serializers
from .models import User, Post, Comment, Group, Follow
from django.shortcuts import render, get_object_or_404


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following = serializers.CharField(source='following.username')

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def create(self, validated_data):
        user_username = validated_data.get('following')['username']
        current_user = get_object_or_404(User, username=user_username)
        validated_data['following'] = current_user
        return Follow.objects.create(**validated_data)

