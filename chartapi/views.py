from .models import Stock_9432
from rest_framework import viewsets
from .serializers import Stock_9432Serializer

class Stock_9432ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stock_9432.objects.all()
    serializer_class = Stock_9432Serializer
