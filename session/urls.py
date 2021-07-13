from django.conf.urls import url
from django.urls import path , include

from .views import SessionDetail,SessionList 

urlpatterns = [
    path('', SessionList.as_view(), name='tickets_list'),
    path('',include('frontend_demo.urls')),
    path('<int:pk>/', SessionDetail.as_view(), name='tickets_detail'),
]
