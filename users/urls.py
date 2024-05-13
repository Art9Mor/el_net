from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

app_name = UsersConfig.name

users_router = routers.SimpleRouter()
users_router.register(r'api/users', UserViewSet, basename='users')

urlpatterns = [
    # User urls
    path('', include(users_router.urls)),

    # Token urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
