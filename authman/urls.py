from django.conf import urls
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path("", views.login_page, name="login"),
    path('auth', include('social_django.urls', namespace='social')),
    path("home", views.login_page, name="home"),
    path('logout', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name = "logout")
]