from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route

from insurance.models import Risk, RiskType, RiskField
from insurance.serializers import RiskSerializer, RiskTypeSerializer


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
    lookup_field = 'name'

    @list_route(methods=['get'], url_path='field-options')
    def field_options(self, request):
        return Response([x[0] for x in RiskField.FIELD_TYPES])
