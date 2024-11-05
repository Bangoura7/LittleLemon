from django.urls import path

from .views import MenuView, ReservationViewSet # Si vous avez des vues à inclure dans les URL




urlpatterns = [
    # Définissez vos chemins ici, par exemple :
    path('menu/', MenuView.as_view() ),

]
