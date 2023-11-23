from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/authentication/', include('authentication.api.urls')),
    path('api/creditManagement/', include('creditManagement.api.urls')),
    path('api/notifications/', include('notifications.api.urls')),
    path('api/savingGoals/', include('savingGoals.api.urls')),
    path('api/transactions/', include('transactions.api.urls')),
]
