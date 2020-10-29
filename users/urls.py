from django.urls import path
from users import views

urlpatterns = [
    path(
        route="login/",
        view=views.login_view,
        name="login"
    ),
    path(
        route="logout/",
        view=views.logout_view,
        name="logout"
    ),
    path(
        route="signup/",
        view=views.signup_view,
        name="signup"
    ),
    path(
        route="profile/update_profile",
        view=views.update_profile_view,
        name="update_profile"
    ),
    path(
        route="profile/<str:username>/",
        view=views.UserProfileView.as_view(),
        name="profile"
    ),
]
