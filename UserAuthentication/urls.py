from django.urls import path
from .views import Registration_Views

urlpatterns = [
    path('register',Registration_Views.as_view(),name='Register'),
]
