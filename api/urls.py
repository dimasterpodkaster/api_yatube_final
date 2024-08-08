from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/?P<post_id>[0-9]+', PostViewSet)
#
router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet)
router.register(r'posts/?P<post_id>[0-9]+/comments/?P<comment_id>[0-9]+', CommentViewSet)
#
router.register('follow', FollowViewSet)
router.register(r'follow/?P<user_id>[0-9]+', FollowViewSet)
#
router.register('group', GroupViewSet)
router.register(r'group/?P<group_id>[0-9]', GroupViewSet)

urlpatterns = [
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('', include(router.urls)),
    ]
