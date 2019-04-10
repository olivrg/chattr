from channels import Group
from django.db import models


class Room(models.Model):

    """
    A chat room
    """
    title = models.CharField(max_length=255)
    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title

    @property
    def websocket_group(self):
        """
        Returns the channels group that sockets should to in order to get sent
        messages as they are generated
        """
        return Group("room-%s" % self.id)
