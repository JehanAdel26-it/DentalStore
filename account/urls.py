from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.login_view,
        name="account_login"
    ),

    path(
        "login/",
        views.login_view,
        name="account_login"
    ),

    path(
        "register/",
        views.register,
        name="account_register"
    ),

    path(
        "profile/",
        views.profile,
        name="account_profile"
    ),

    path(
        "logout/",
        views.logout_view,
        name="account_logout"
    ),

]