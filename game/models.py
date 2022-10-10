from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_string = models.TextField(max_length=6, default = "")

    def _str__(self):
        return self.id

    def updateBoard(self):
        # Boards.objects.filter(id=id).update(game_string=Concat
        pass

    class Meta:
        db_table = "Boards"