
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path
from django.conf.urls import url, include



urlpatterns = [
#***********************************Protected*****************************************************************

          #------------------------------------GATEWAY---------------------------------------#
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),
    path('api/logout', views.LogoutAPI.as_view(), name='logout_api'),
    # url('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('api/reset_password', views.LogoutAPI, name='logout_api'),
    # path('api/reset_password/confirm', views.LogoutAPI, name='logout_api'),


          #------------------------------------DASHBOARD---------------------------------------#
    path('api/ios-healthkit-uploads', views.AppleHealthKitUploadAPI.as_view(), name='ios-healthkit-uploads'),
    path('api/list',views.AppleHealthKitListDataAPI.as_view()),
    path('api/list/ios-healthkit-uploads', views.AppleHealthKitListUploadAPI.as_view()),

#***********************************Protected*****************************************************************



#***********************************Un-Protected**************************************************************

    path('api/dashboard', views.DashboardAPI.as_view()),
    # path('api/chart/data/<str:attribute_name>', views.ChartDataAPI.as_view())
    path('api/user-profile/retrieve', views.UserprofileRetrieveAPI.as_view(), name='user-profile-retrieve'),
    path('api/user-profile/update', views.UserprofileUpdateAPI.as_view(), name='user-profile-update'),

#***********************************Un-Protected**************************************************************

]
