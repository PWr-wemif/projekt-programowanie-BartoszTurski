from django.db import models


class Card(models.Model):
    #m = max, c = current
    MHP = models.IntegerField()
    CHP = models.IntegerField()
    Name = models.TextField()
    Class = models.TextField()
    Race = models.TextField()
    Level = models.IntegerField()
    Strenght = models.IntegerField()
    Dexterity = models.IntegerField()
    Constitution = models.IntegerField()
    Inteligence = models.IntegerField()
    Wisdom = models.IntegerField()
    Charisma = models.IntegerField()
    # saving throws
    StrST = models.IntegerField()
    DexST = models.IntegerField()
    ConST = models.IntegerField()
    IntST = models.IntegerField()
    WisST = models.IntegerField()
    #hit dices
    Mhitdice = models.IntegerField()
    Chitdice = models.IntegerField()
    #death saves
    Dsp = models.IntegerField()
    Dsf = models.IntegerField()
    Skills = models.TextField()
    Proficiencies = models.TextField()
    Spells = models.TextField()
    Inventory = models.TextField()




