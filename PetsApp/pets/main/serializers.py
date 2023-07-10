from rest_framework import serializers
from .models import Pet


class PetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'vin', 'user')


class PetDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pet
        fields = '__all__'
