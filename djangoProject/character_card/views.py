from django.shortcuts import render
from .models import Character

def character_view(request):
    if request.method == 'POST':

        data = request.POST


        character = Character.objects.create(
            user=request.user,
            name=data.get('name'),
            race=data.get('race'),
            class_name=data.get('class'),
            level=data.get('level'),
            strength=data.get('strength'),
            dexterity=data.get('dexterity'),
            constitution=data.get('constitution'),
            intelligence=data.get('intelligence'),
            wisdom=data.get('wisdom'),
            charisma=data.get('charisma'),
            StrST=data.get('StrST'),
            DexST=data.get('DexST'),
            ConST=data.get('ConST'),
            IntST=data.get('IntST'),
            WisST=data.get('WisST'),
            Mhitdice=data.get('Mhitdice'),
            Chitdice=data.get('Chitdice'),
            Dsp=data.get('Dsp'),
            Dsf=data.get('Dsf'),
            skills=data.get('skills'),
            proficiencies=data.get('proficiencies'),
            spells=data.get('spells'),
            inventory=data.get('inventory'),
        )

        # Zapisujemy obiekt do bazy danych
        character.save()

    # Pobieramy postać zalogowanego użytkownika
    character = Character.objects.filter(user=request.user).first()

    return render(request, 'character_card/character_form.html', {'character': character})
