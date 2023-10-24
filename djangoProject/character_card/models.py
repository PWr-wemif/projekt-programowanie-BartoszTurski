from django.db import models

class Card(models.Model):
    #m = max, c = current
    MHP =models.IntegerField(max_length=2)
    CHP =models.IntegerField(max_length=2)
    Name =models.TextField(max_lenght=20)
    Class =models.TextField(max_lenght=20)
    Race =models.TextField(max_lenght=20)
    Level =models.IntegerField(max_length=2)
    Strenght =models.IntegerField(max_length=2)
    Dexterity =models.IntegerField(max_length=2)
    Constitution =models.IntegerField(max_length=2)
    Inteligence =models.IntegerField(max_length=2)
    Wisdom =models.IntegerField(max_length=2)
    Charisma =models.IntegerField(max_length=2)
    # saving throws
    StrST =models.IntegerField(max_length=2)
    DexST =models.IntegerField(max_length=2)
    ConST =models.IntegerField(max_length=2)
    IntST =models.IntegerField(max_length=2)
    WisST =models.IntegerField(max_length=2)
    #hit dices
    Mhitdice =models.IntegerField(max_length=2)
    Chitdice =models.IntegerField(max_length=2)
    #death saves
    Dsp =models.IntegerField(max_length=2)
    Dsf =models.IntegerField(max_length=2)
    Skills =models.TextField(max_lenght=200)
    Proficiencies =models.TextField(max_lenght=200)
    Spells =models.TextField(max_lenght=200)
    Inventory =models.TextField(max_lenght=20)



# Create your models here.
