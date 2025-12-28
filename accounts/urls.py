from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, profile_view, profile_edit

urlpatterns = [
    # Signup (registro)
    path("signup/", SignUpView.as_view(), name="signup"),

    # Login / Logout (CBV de Django)
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Perfil de usuario
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),
]
