from django.urls import path
from .views import CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (UserRegisterView,
                    LogoutView,
                    LoginUser,
                    CodeVerificationView,
                        # vistas para el reseteo del password
                    CustomPasswordResetView,
                    CustomPasswordResetDoneView,
                    CustomPasswordResetConfirmView,
                    CustomPasswordResetCompleteView,
                    logout_view
                    )

app_name = "users_app"


urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='token_revocado'),
    # rutas normales sin la api
   path('register/', UserRegisterView.as_view(), name='user-register',),
    path(
        'login/', 
        LoginUser.as_view(),
        name='user-login',
    ),
       path(
        'user-verification/<int:pk>/', 
        CodeVerificationView.as_view(),
        name='user-verification',
    ),
    path('logout/', logout_view, name='logout'),
    # rutas usadas para el cambio de la contraseña
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
