from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acted_notifications')
    verb = models.CharField(max_length=100)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor.username} {self.verb} {self.target} for {self.recipient.username}"


# In the posts app, create a Like model that tracks which users have liked which posts. This model should have a ForeignKey to Post and a ForeignKey to User.
# In a new app called notifications, create a Notification model with fields like recipient (ForeignKey to User), actor (ForeignKey to User), verb (describing the action), target (GenericForeignKey to the object), and timestamp.

