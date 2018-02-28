from rest_framework import viewsets
from insurance.models import Risk, RiskType
from insurance.serializers import RiskSerializer, RiskTypeSerializer


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
