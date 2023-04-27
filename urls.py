from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
urlpatterns = router.urls
