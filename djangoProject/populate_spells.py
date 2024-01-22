import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from character_card.models import CharacterClass, Spell

# Define the spells for each class
class_spells = {
    "Barbarian": [],
    "Bard": ["Charm Person", "Dissonant Whispers", "Healing Word", "Vicious Mockery"],
    "Cleric": ["Cure Wounds", "Guiding Bolt", "Protection from Evil and Good", "Spiritual Weapon"],
    "Druid": ["Entangle", "Healing Word", "Moonbeam", "Shillelagh"],
    "Fighter": ["Shield", "Magic Missile", "Absorb Elements", "Find Familiar"],
    "Monk": ["Fangs of the Fire Snake", "Sweeping Cinder Strike", "Water Whip"],
    "Paladin": ["Divine Smite", "Lay on Hands", "Shield of Faith", "Wrathful Smite"],
    "Ranger": ["Hunter's Mark", "Hail of Thorns", "Animal Friendship", "Speak with Animals"],
    "Rogue": ["Mage Hand", "Invisibility", "Sleep", "Color Spray"],
    "Sorcerer": ["Fireball", "Lightning Bolt", "Charm Person", "Magic Missile"],
    "Warlock": ["Eldritch Blast", "Hellish Rebuke", "Hex", "Pact of the Chain"],
    "Wizard": ["Fireball", "Teleport", "Shield", "Mage Armor", "Identify"]
}

for class_name, spells in class_spells.items():
    character_class, created = CharacterClass.objects.get_or_create(name=class_name)
    for spell_name in spells:
        spell, created = Spell.objects.get_or_create(name=spell_name)
        character_class.spells.add(spell)

print("Spells populated successfully.")
