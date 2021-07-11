from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ticket
from .serializers import TicketSerializer

class TicketsList(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
