from django.db import models

# Create your models here.
class StockRating(models.Model):
    #title
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) #description
    value = models.FloatField()
    #completed
    created_at = models.DateTimeField(auto_now_add=True) #created_at

    def __str__(self):
        #return the stock rating title
        return self.title