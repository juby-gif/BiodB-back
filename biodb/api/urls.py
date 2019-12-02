
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path
from django.conf.urls import url, include



urlpatterns = [
#------------------------------------GATEWAY---------------------------------------#
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),
    path('api/logout', views.LogoutAPI.as_view(), name='logout_api'),
    # url('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('api/reset_password', views.LogoutAPI, name='logout_api'),
    # path('api/reset_password/confirm', views.LogoutAPI, name='logout_api'),

#------------------------------------Extracting---------------------------------------#
    path('api/ios-healthkit-uploads', views.AppleHealthKitUploadAPIView.as_view(), name='ios-healthkit-uploads'),
]
