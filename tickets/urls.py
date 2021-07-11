from django.urls import path
from .views import TicketsList, TicketsDetail

urlpatterns = [
    path('', TicketsList.as_view(), name='tickets_list'),
    path('<int:pk>/', TicketsDetail.as_view(), name='tickets_detail'),
]
