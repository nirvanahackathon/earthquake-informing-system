from django.db import models

class Regions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    region_name = models.CharField()

    def __str__(self):
        return self.region_name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Tweets(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    person_name = models.CharField(max_length=100, null=True, blank=True)
    region_id = models.ForeignKey(Regions, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"