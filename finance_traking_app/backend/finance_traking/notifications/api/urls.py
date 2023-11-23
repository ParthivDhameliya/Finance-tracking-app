from django.urls import path
from notifications.api.views import test

urlpatterns = [
    path('test/', test),
]
