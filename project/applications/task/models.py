from django.db import models
# from ckeditor.fields import RichTextFields
from applications.state.models import State

# Create your models here.
class Task(models.Model):
    name = models.CharField(("Name"), max_length=30, null=False, blank=False)
    # Can't use the RichTextFields by a problem importing it from ckeditor
    # description = RichTextFields(("Description"), max_length=150) # Gives the tools for the input of the text
    description = models.CharField(("Description"), max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + ' ' + self.state