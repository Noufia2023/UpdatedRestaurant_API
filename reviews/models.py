
from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator,MaxValueValidator

#Creating Restaurant Model           
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    average_rating = models.FloatField(default=0)

#Calculate and update the value of average rating based on the assocaiated reviews
    def update_average_rating(self):
        self.average_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.save()
        
    def __str__(self):
        return self.name   

#Creating Review Model
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
    ])
    comment = models.TextField()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.restaurant.update_average_rating()

    def __str__(self):
        return f'review for {self.restaurant.name}'
     

    
 