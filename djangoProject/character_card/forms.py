from django import forms
from .models import Character, Race, CharacterClass, Skill, Spell, InventoryItem

class CharacterForm(forms.ModelForm):
    race = forms.ModelChoiceField(queryset=Race.objects.all(), required=False)
    character_class = forms.ModelChoiceField(queryset=CharacterClass.objects.all(), required=False)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    spells = forms.ModelMultipleChoiceField(queryset=Spell.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    inventory_items = forms.ModelMultipleChoiceField(queryset=InventoryItem.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Character
        fields = ['user', 'name', 'race', 'character_class', 'level', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'StrST', 'DexST', 'ConST', 'IntST', 'WisST', 'Mhitdice', 'Chitdice', 'Dsp', 'Dsf', 'skills', 'spells', 'inventory_items']

