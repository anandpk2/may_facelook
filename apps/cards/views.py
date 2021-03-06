from django.shortcuts import render
from django.core.context_processors import csrf
from .models import Cards
# Create your views here.


def home(request):
    """Display all cards."""
    context = {}
    cards = Cards.objects.all()
    context = {'cards': cards}
    template = 'home.html'
    return render(request, template, context)


def view_card(request, card_id):
    """Display specific card."""
    context = {}
    card = Cards.objects.get(id=card_id)
    context = {'card': card}
    template = 'view_card.html'
    return render(request, template, context)


def create_card(request):
    """Creating new cards."""
    context = {}
    if request.method == 'POST':
        try:

            card_title = request.POST.get('card_title')
            card_description = request.POST.get('card_description')
            card_picture = request.FILES.get('card_picture')
            try:
                created_by = request.user
            except:
                created_by = None

            if created_by is not None:
                card_info = Cards(
                    card_title=card_title,
                    user=created_by,
                    card_description=card_description,
                    card_hero_image=card_picture)
            else:
                card_info = Cards(
                    card_title=card_title,
                    card_description=card_description,
                    card_hero_image=card_picture)

            card_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    template = "create_card.html"
    return render(request, template, context)
