from django.contrib.auth.models import User
from django.db import models
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




class Spell(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    learned = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class CharacterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    spells = models.ManyToManyField(Spell, related_name='classes')

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True, blank=True)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.SET_NULL, null=True, blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    class_name = models.CharField(max_length=100, default='DefaultClassName')
    StrST = models.IntegerField()
    DexST = models.IntegerField()
    ConST = models.IntegerField()
    IntST = models.IntegerField()
    WisST = models.IntegerField()
    Mhitdice = models.IntegerField()
    Chitdice = models.IntegerField()
    Dsp = models.IntegerField()
    Dsf = models.IntegerField()
    skills = models.ManyToManyField(Skill, blank=True)
    spells = models.ManyToManyField(Spell, blank=True)
    inventory = models.ManyToManyField('InventoryItem', related_name='characters_for_inventory')
    inventory_items = models.ManyToManyField('InventoryItem', related_name='characters_for_inventory_items')
