from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'articles', views.ArticlesViewSet)
router.register(r'comments', views.CommentsViewSet)
router.register(r'category', views.CategorysViewSet)
router.register(r'article_category', views.Article_CategorysViewSet)
router.register(r'tags', views.TagsViewSet)
router.register(r'article_tags', views.Article_TagsViewSet)
router.register(r'user_views', views.User_ViewsViewSet)

# router.register(r'comments', views.CommentViewSet)
# router.register(r'users', views.UserList)
# router.register(r'thethao', views.PostViewSetCategory)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls