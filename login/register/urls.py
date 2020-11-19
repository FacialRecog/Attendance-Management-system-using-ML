
from django.urls import path,include
from django.conf.urls import include, url
from .views import registerlist
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from register import views


urlpatterns = [
    path('register/', registerlist),
     path('register/<int:pk>/', views.login_detail),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
]
