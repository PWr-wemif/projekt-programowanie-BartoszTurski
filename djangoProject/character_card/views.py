from .models import Character
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import CharacterForm
from .models import Character
from django.shortcuts import render, redirect, get_object_or_404


def list_characters(request):
    if not request.user.is_authenticated:
        return redirect('login')

    characters = Character.objects.filter(user=request.user)
    return render(request, 'character_card/list_characters.html', {'characters': characters})

def character_edit(request, character_id=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if character_id:
        character = get_object_or_404(Character, id=character_id, user=request.user)
        if request.method == 'POST':
            form = CharacterForm(request.POST, instance=character)
            if form.is_valid():
                form.save()
                return redirect('character_card:character_view', character.id)
        else:
            form = CharacterForm(instance=character)
    else:
        if request.method == 'POST':
            form = CharacterForm(request.POST)
            if form.is_valid():
                new_character = form.save(commit=False)
                new_character.user = request.user
                new_character.save()
                return redirect('character_card:character_view', new_character.id)
        else:
            form = CharacterForm()

    return render(request, 'character_card/character_edit.html', {'form': form})

def character_view(request, character_id):
    if not request.user.is_authenticated:
        return redirect('login')

    character = get_object_or_404(Character, id=character_id, user=request.user)
    return render(request, 'character_card/characterview.html', {'character': character})
