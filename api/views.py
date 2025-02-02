from rest_framework import viewsets, status, permissions
from api.models import Post, Comment, Group, Follow, User
from api.serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from api.permissions import IsAuthorOrReadOnly
from api.pagination import CustomPagination
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Post.objects.all()
        text = self.request.query_params.get('text', None)
        group = self.request.query_params.get('group', None)
        if text is not None:
            queryset = queryset.filter(text=text)
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request):
        posts = self.get_queryset().all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        posts = self.queryset.all()
        post = get_object_or_404(posts, id=pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        posts = self.queryset.all()
        post = get_object_or_404(posts, id=pk)
        if request.user == post.author:
            serializer = self.get_serializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        posts = self.queryset.all()
        post = get_object_or_404(posts, id=pk)
        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        posts = self.queryset.all()
        post = get_object_or_404(posts, id=pk)
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, post_id=None):
        comments = Comment.objects.filter(post=post_id)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, post_id=None):
        data = request.data
        _mutable = data._mutable
        data._mutable = True
        request.data['post'] = post_id
        data._mutable = _mutable
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, post_id=None, pk=None):
        comments = self.queryset.all()
        comment = get_object_or_404(comments, id=pk)
        serializer = self.get_serializer(comment)
        return Response(serializer.data)

    def update(self, request, post_id=None, pk=None):
        comments = self.queryset.all()
        comment = get_object_or_404(comments, id=pk)
        if request.user == comment.author:
            serializer = self.get_serializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, post_id=None, pk=None):
        comments = self.queryset.all()
        comment = get_object_or_404(comments, id=pk)
        if request.user == comment.author:
            serializer = self.get_serializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, post_id=None, pk=None):
        comments = self.queryset.all()
        comment = get_object_or_404(comments, id=pk)
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        groups = self.queryset.all()
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        _mutable = data._mutable
        data._mutable = True
        group_title = request.data.get('title')
        groups_same_title = Group.objects.filter(title=group_title).count()
        if group_title:
            group_slug = slugify(group_title + str(groups_same_title))
        else:
            group_slug = slugify(str(groups_same_title))
        request.data['slug'] = group_slug
        data._mutable = _mutable
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Follow.objects.all()
        aim = self.request.query_params.get('search', None)
        if aim is not None:
            queryset = queryset.filter(user__username=aim)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        follows = self.get_queryset().all()
        serializer = self.get_serializer(follows, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_username = data.get('following')
            current_user = get_object_or_404(User, username=user_username)
            find_subscibtion = Follow.objects.filter(user=request.user, following=current_user.id)
            if not find_subscibtion:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        follows = self.queryset.all()
        follow = get_object_or_404(follows, id=pk)
        if request.user == follow.user:
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
