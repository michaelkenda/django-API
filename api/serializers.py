from .models import stock
from rest_framework import serializers

class stockserializer(serializers.ModelSerializer):
    class Meta:
        model = stock
        fields = (
            'id',
            'name',
            'password1',
            'password2'
        )