from .models import Character
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import CharacterForm
from .models import Character, Spell, CharacterClass, Race, Profession, Skill, InventoryItem
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse


def list_characters(request):
    if not request.user.is_authenticated:
        return redirect('login')

    characters = Character.objects.filter(user=request.user)
    return render(request, 'character_card/list_characters.html', {'characters': characters})
def load_spells(request):
    character_class_id = request.GET.get('character_class_id')
    spells = Spell.objects.filter(classes__id=character_class_id).order_by('name') if character_class_id else Spell.objects.none()
    spell_data = [{'id': spell.id, 'name': spell.name} for spell in spells]
    return JsonResponse(spell_data, safe=False)
def character_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            form.save_m2m()
            return redirect('character_card:list_characters')

    else:
        form = CharacterForm()

    return render(request, 'character_card/character_create.html', {'form': form})

def character_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    character = get_object_or_404(Character, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        spells = request.POST.getlist("spell")
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            form.save_m2m()
            for i in Spell.objects.all():
                i.learned = False
                i.save()
            for spell in spells:
                spell = Spell.objects.get(id=spell)
                spell.learned=True
                spell.save()
            return redirect(reverse('character_card:character_detail', args=[character.id]))
    else:
        form = CharacterForm(instance=character)

    return render(request, 'character_card/character_edit.html', {'form': form, 'character': character})

def character_view(request, character_id):
    if not request.user.is_authenticated:
        return redirect('login')

    character = get_object_or_404(Character, pk=character_id)
    context = {
        'character': character
    }
    return render(request, 'character_card/characterview.html', context)
