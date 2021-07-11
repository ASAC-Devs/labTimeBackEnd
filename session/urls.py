from django.urls import path

from .views import SessionDetail,SessionList 

urlpatterns = [
    path('', SessionList.as_view(), name='tickets_list'),
    path('<int:pk>/', SessionDetail.as_view(), name='tickets_detail'),
]
