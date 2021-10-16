from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



api_urls=[
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]





app_name='accounts'
urlpatterns=[
    path('register/', views.UserRegisteration.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', views.Dashboard.as_view(), name='dashboard'),
    path('api/', include(api_urls))



    
]