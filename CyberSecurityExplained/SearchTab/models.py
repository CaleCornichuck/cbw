from django.db import models

class Site(models.Model):
    name = models.CharField('Section Name', max_length=120)
    link = models.CharField('Link', max_length=1000)

    def __str__(self):
        return self.name
    
