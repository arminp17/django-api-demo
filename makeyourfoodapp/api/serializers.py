from rest_framework import serializers
from .models import Appmodel


class AppmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appmodel
        fields = ['userId', 'id', 'title', 'body']