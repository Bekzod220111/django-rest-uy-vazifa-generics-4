from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Qale
from .serializers import QaleSerializer


class QaleApiView(ListCreateAPIView):
    queryset = Qale.objects.all()
    serializer_class = QaleSerializer


class QaleDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Qale.objects.all()
    serializer_class = QaleSerializer