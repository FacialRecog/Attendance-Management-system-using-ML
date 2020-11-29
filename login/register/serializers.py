from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Register
from .models import Attendance

class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class Attendanceserializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'