from django.contrib import admin
from .models import Team, Player


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "last_name", "age", "team"]
    list_editable = ["team"]
    list_display_links = ["name"]


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)