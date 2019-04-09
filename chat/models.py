from django.db import models


class Room(models.Model):

    """
    A chat room
    """
    title = models.CharField(max_length=255)
    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title
