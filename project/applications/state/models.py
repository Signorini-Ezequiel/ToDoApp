from django.db import models

# Create your models here.
class States(models.Model):
    STATE_CHOICES = (
        ('0', 'To do'),
        ('1', 'Doing'),
        ('2', 'Done')
    )
    state = models.CharField(("State name"), null=False, blank=False)
    
    def __str__(self):
        return self.name