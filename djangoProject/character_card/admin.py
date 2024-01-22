from django.contrib import admin
from .models import Character, Skill, Spell, InventoryItem

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'display_skills', 'display_spells', 'display_inventory_items')

    def display_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    display_skills.short_description = 'Skills'

    def display_spells(self, obj):
        return ", ".join([spell.name for spell in obj.spells.all()])
    display_spells.short_description = 'Spells'

    def display_inventory_items(self, obj):
        return ", ".join([item.name for item in obj.inventory_items.all()])
    display_inventory_items.short_description = 'Inventory Items'

# Register your models here.
admin.site.register(Character, CharacterAdmin)

# Optional: If you want to manage Skills, Spells, and InventoryItems in the admin
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(InventoryItem)
