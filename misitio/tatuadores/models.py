from django.db import models

class Notice(models.Model):
    name_Notice = models.CharField(max_length = 255)
    content_Notice = models.CharField(max_length = 255)

        

