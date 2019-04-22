from rest_framework import serializers
from .models import peoples

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model=peoples
        fields=('firstname', 'lastname')
