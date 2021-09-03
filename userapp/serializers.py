from django.db import models
from userapp.models import employees
from rest_framework import serializers

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ('firstname','lastname')
        # fields = '__all__'