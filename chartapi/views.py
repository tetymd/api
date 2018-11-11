from .models import Chart
from rest_framework import viewsets
from .serializers import ChartSerializer

class ChartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
