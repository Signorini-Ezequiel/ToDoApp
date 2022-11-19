from django.db import models

# Create your models here.
class State(models.Model):
    STATE_CHOICES = (
        ('0', 'To do'),
        ('1', 'Doing'),
        ('2', 'Done')
    )
    state = models.CharField(("State name"), max_length=5, null=False, blank=False, choices=STATE_CHOICES)
    
    def __str__(self):
        return self.state