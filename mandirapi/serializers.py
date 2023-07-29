from rest_framework import serializers
from .models import MandirModel

class MandirSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandirModel
        fields = '__all__'