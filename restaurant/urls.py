from django.urls import path
from . import views  # Si vous avez des vues à inclure dans les URL

urlpatterns = [
    # Définissez vos chemins ici, par exemple :
    path('', views.index1, name='index'),
]
