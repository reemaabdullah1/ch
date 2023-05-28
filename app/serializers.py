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

class LoginFormSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        return data
    
    
class TranslatorUpdateProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    firstLanguage = serializers.CharField(required=False, source='First_Language')
    secondLanguage = serializers.CharField(required=False, source='Second_Language')
    bio = serializers.CharField(required=False, allow_blank=True)

    def update(self, instance, validated_data):
        # Access the old data for the user.
        try:
            user = User.objects.get(username=validated_data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("There is no user with this username")

        try:
            translator = Translatorr.objects.get(user=user)
        except Translatorr.DoesNotExist:
            raise serializers.ValidationError("There is no translator with this username")

        # Update the data.
        if 'name' in validated_data:
            translator.name = validated_data['name']
        if 'age' in validated_data:
            translator.age = validated_data['age']
        if 'email' in validated_data:
            user.email = validated_data['email']
        if 'phone' in validated_data:
            translator.phoneNumber = validated_data['phone']
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        if 'firstLanguage' in validated_data:
            translator.First_Language = validated_data['firstLanguage']
        if 'secondLanguage' in validated_data:
            translator.Second_Language = validated_data['secondLanguage']
        if 'bio' in validated_data:
            translator.Bio = validated_data['bio']

        # Save the data.
        user.save()
        translator.save()

        return {'message': 'Your information saved successfully'}