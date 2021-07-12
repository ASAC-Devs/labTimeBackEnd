# from django.urls import path
# from .views import CustomUserCreate, BlacklistTokenUpdateView

# app_name = 'users'

# urlpatterns = [
#     path('create/', CustomUserCreate.as_view(), name="create_user"),
#     path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
#          name='blacklist')
# ]




from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path("", ProfileList.as_view(), name="profile_list"),
    path("<int:pk>/", ProfileDetail.as_view(), name="profile_detail"),
]