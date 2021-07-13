from django.urls import path
from .views import ProfileList, ProfileDetail , SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView

urlpatterns = [
    path("", ProfileList.as_view(), name="profile_list"),
    path("<int:pk>", ProfileDetail.as_view(), name="profile_detail"),
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view())
]