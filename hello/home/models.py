from django.db import models

# Create your models here.
# makemigrations -> create changes and store in a file 
# migrate -> apply the pending chenges created by makemigrations 

# defining class for form data input
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    # in database changing the data name with name
    def __str__(self):
        return self.name