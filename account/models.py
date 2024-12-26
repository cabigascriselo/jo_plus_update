from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_pmd = models.BooleanField('Plant Maintenance', default=False)
    is_eid = models.BooleanField('Electrical and Instrument', default=False)
    is_uto = models.BooleanField('Utilities Operation', default=False)
    is_qa = models.BooleanField('Quality Assurance', default=False)




