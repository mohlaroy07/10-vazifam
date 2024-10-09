from django.shortcuts import render
from .models import Team, Player


def teams_page(request):
    
    if request.method == "POST":
        name = request.POST["jamoa_nomi"]
        description = request.POST["jamoa_haqida"]

        print(name, description)

        yangi_jamoa = Team.objects.create(name=name, description=description)

    teams = Team.objects.all()

    context = {"teams": teams}

    return render(request, "team.html", context)


def players_page(request):

    if request.method == "POST":
        name = request.POST["oyinchi_ismi"]
        last_name = request.POST["oyinchi_familiyasi"]
        age = request.POST["oyinchi_yoshi"]
        team = request.POST["oyinchi_jamoasi"]

        print(name, last_name, age, team)

        yangi_oyinchi = Player.objects.create(name=name, last_name=last_name, age=age, team_id=team)

    players = Player.objects.all()

    context = {"players": players}

    return render(request, "player.html", context)