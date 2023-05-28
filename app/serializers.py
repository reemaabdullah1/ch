import stripe
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product, User, Customer, Appointment,Translatorr

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutSessionSerializer(serializers.ModelSerializer):
    Product_id = serializers.CharField(max_length=150)
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["Product"]

    def check_session(self, sid):
        try:
            proudct = stripe.checkout.Session.retrieve(sid)
        except stripe.error.StripeError as e:
            raise ValidationError(e)
        return proudct
    
    def validate(self, attrs):
        proudct = self.check_session(attrs.pop("Product_id"))
        attrs["Product"] = proudct
        return super().validate(attrs)
    
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

