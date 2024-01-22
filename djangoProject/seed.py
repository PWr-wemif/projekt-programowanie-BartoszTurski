import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from character_card.models import CharacterClass, Race, Profession, Skill, InventoryItem

def add_data(model, data_list):
    for name in data_list:
        obj, created = model.objects.get_or_create(name=name, description=name + " description")
        if created:
            print(f"Added: {obj.name}")

def populate_character_classes():
    class_names = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Mystic", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    add_data(CharacterClass, class_names)

def populate_races():
    race_names = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    add_data(Race, race_names)

def populate_professions():
    profession_names = ["Apothecary", "Boater", "Bookkeeper", "Brewer", "Cook", "Driver", "Farmer", "Fisher", "Guide", "Herbalist", "Herder", "Hunter", "Innkeeper", "Lumberjack", "Miller", "Miner", "Porter", "Rancher", "Sailor", "Scribe", "Siege Engineer", "Stablehand", "Tanner", "Teamster", "Woodcutter"]
    add_data(Profession, profession_names)

def populate_skills():
    skill_names = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
    add_data(Skill, skill_names)

def populate_inventory_items():
    item_names = ["Blackrazor", "Moonblade", "Ring of Three Wishes", "Luck Blade", "Tome of the Stilled Tongue", "Vorpal Sword", "Wave", "Robe of the Archmagi", "Holy Avenger", "Staff of the Magi", "Talisman of Ultimate Evil", "Talisman of Pure Good", "Belt of Storm Giant Strength", "Sun Blade", "Instrument of the Bards", "Flame Tongue", "Fizban’s Treasury of Dragons items", "Bracers of Archery", "Deck of Many Things", "Bag of Holding"]
    add_data(InventoryItem, item_names)

if __name__ == "__main__":
    populate_character_classes()
    populate_races()
    populate_professions()
    populate_skills()
    populate_inventory_items()
