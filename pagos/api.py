from django_filters.rest_framework import DjangoFilterBackend
from .models import Pagos
from rest_framework import viewsets
from .serializers import PagoSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('usuario__id', 'fecha_pago', 'servicio')

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'