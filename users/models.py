from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False)
    email         = models.CharField(max_length=100, unique=True)
    password      = models.CharField(max_length=256)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email
