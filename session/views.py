from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Session
from .serializers import SessionSerializer

class SessionList(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
