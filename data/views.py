from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Record, High_school,Accolade
from .forms import PlayerForm


# Create your views here.

def soccer(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'index.html', context)


def map(request):
    HS = High_school.objects.filter(id = '25')
    loc = 'https://image.maps.api.here.com/mia/1.6/mapview?app_id=uk8guHgE21xY86cZaH49&app_code=aSDqpsTFx1E1yvZRqKa8BQ&ctr=40.113349,%20-96.485571&w=720&h=440&z=4'
    poi = '&poi='
    for h in HS:
        poi += str(h.location_lat)+','+str(h.location_long)+','

    context = {
        'src': loc+poi
    }
    return render(request, 'map.html', context)


def search(request):
    if request.method == "POST":
        #     print(request.POST)
        form = PlayerForm(request.POST)
        players = Player.objects.all()
        #first_name = request.POST['first_name']
        '''if first_name:
            players = players.filter(first_name=first_name)'''

        league_id = request.POST['League']
        position_id = request.POST['Positions']
        year_id = request.POST['Starter_Year']
        all_id = request.POST['All_Conference_Year']

        if position_id and position_id != '0':
            players = players.filter(id__in = Record.objects.filter(Position1=int(position_id)).values_list('Player_id'))

        if league_id and league_id != '0':
            players = players.filter(College__College_League=int(league_id)).order_by('id')

        if year_id and year_id != '0':
            from django.db.models import Count
            starter_record = Record.objects.filter(Is_starter=True).values('Player_id').annotate(total = Count('Player_id')).filter(total = year_id)
            players = players.filter(id__in = starter_record.values_list('Player_id'))


        if all_id and all_id != '0':
            from django.db.models import Count
            all_acc = Accolade.objects.values('Player_id').annotate(total = Count('Player_id')).filter(total = all_id)
            players = players.filter(id__in = all_acc.values_list('Player_id'))


        HS = High_school.objects.filter(id__in=players.values_list('High_School_id'))

        loc = 'https://image.maps.api.here.com/mia/1.6/mapview?app_id=uk8guHgE21xY86cZaH49&app_code=aSDqpsTFx1E1yvZRqKa8BQ&ctr=40.113349,%20-96.485571&w=720&h=440&z=4'
        poi = '&poi='
        for h in HS:
            poi += str(h.location_lat) + ',' + str(h.location_long) + ','


        return render(request, 'search.html',{'players': players, 'form': form,'src': loc + poi})
    form = PlayerForm()
    return render(request, 'search.html', {'form': form})