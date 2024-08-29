from rest_framework import serializers
from .models import Compliment


class ComplimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliment
        fields = ['id', 'text', 'compliment_type']