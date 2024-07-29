from django.urls import path
from . import views
urlpatterns = [
    path("",views.login__sys,name="home"),
    path("login/",views.login__sys,name="login"),
    path("signup/",views.signup_sys,name="signup"),
    path("dashboard/",views.dashboard_page,name="dashboard"),
    path("logout/",views.logout_page,name="logout")
]
