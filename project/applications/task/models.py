from django.db import models
from ckeditor.fields import RichTextFields
from applications.state.models import States

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(("Name"), max_length=30)
    description = RichTextFields(("Description"), max_length=150) # Gives the tools for the input of the text
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + ' ' + self.state