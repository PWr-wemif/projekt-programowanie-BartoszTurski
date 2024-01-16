from django.urls import path
from . import views  # importuj swoje widoki

app_name = 'dice_roller'  # dodajemy przestrzeń nazw

urlpatterns = [
    path('<int:character>', views.roll_dice, name='roll_dice'),  # ścieżka do widoku roll_dice
]
