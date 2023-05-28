from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Customer, Appointment,Translatorr

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_customer', 'is_translator','is_Admin')

        
class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translatorr
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        

from rest_framework import serializers
from django.contrib.auth import authenticate


from rest_framework import serializers
from django.contrib.auth import authenticate

