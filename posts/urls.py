from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet,UserActiveViewSet,LikeViews


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'users-info', UserActiveViewSet)
router.register(r'likes-info', LikeViews)

urlpatterns = router.urls