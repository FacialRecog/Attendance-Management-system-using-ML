from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Register

class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

