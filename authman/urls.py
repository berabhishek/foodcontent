from django.conf import urls
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path("<str:product_name>/", views.login_page, name="view_product"),
    path("", views.login_page, name="login"),
    path('auth', include('social_django.urls', namespace='social')),
    path('logout', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name = "logout"),
    path('add_data', views.add_data, name="add_data")
]