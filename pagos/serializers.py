from rest_framework import serializers
from .models import Pagos
from rest_framework import generics




class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = '__all__',
