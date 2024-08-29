from django.shortcuts import render

from rest_framework import generics
from .models import Compliment
from .serializers import ComplimentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ComplimentList(generics.ListAPIView):
    queryset = Compliment.objects.all()
    serializer_class = ComplimentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['compliment_type']