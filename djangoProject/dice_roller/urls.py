# dice_roller/urls.py
from django.urls import path
from .views import roll_dice

app_name = 'dice_roller'

urlpatterns = [
    path('roll_dice/', roll_dice, name='roll_dice'),
]
