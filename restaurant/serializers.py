from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reservation, Menu


# Serialisation du model User defini par defaut 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        field =  '__all__'
# Serialisation de la Class Reservation 
class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'

# Serialisation de la Class Reservation 
class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = '__all__'