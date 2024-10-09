from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Player(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.age}"