from django.shortcuts import render
from random import randint

def roll_dice(request, character):
    if request.method == 'POST':
        num_dice = int(request.POST.get('num_dice', 1))
        num_sides = int(request.POST.get('num_sides', 6))

        rolls = [randint(1, num_sides) for _ in range(num_dice)]

        context = {
            'rolls': rolls,
            'num_dice': num_dice,
            'num_sides': num_sides,
            'character': character  # Include the character variable
        }
        return render(request, 'dice_roller/roll_dice.html', context)

    return render(request, 'dice_roller/roll_dice.html', {'character': character})
