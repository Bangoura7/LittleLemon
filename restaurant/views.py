from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from django.contrib.auth.models import User
from .models import Reservation, Menu
from django.contrib.auth.models import Permission
from .serializers import ReservationSerializer,MenuSerializer, UserSerializer
# Create your views here.


#Creation de la vue pour l'affichage des reservations
class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
   

# Creation de Menu
class MenuView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Succès", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "Échec", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]  # Utilise la permission personnalisée