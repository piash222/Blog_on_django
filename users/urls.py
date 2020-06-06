from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_view.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password-reset"),
    path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),

    path("profile/", views.profile, name="profile")

]
