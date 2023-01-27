from django.db import models

class  SiteUrl (models.Model):
    
    endpoint = models.CharField(max_length=80)


