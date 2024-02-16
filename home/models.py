from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    city = models.CharField(max_length=200, default='')
    venuname = models.CharField(max_length=200, help_text='add venue name', default='')
    name = models.CharField(max_length=200,default='',verbose_name='movie name')
    discription = models.TextField(default='')
    slug = models.SlugField(unique=True)
    platinum_seats = models.IntegerField(default=0)
    gold_seats = models.IntegerField(default=0)
    silver_seats = models.IntegerField(default=0)
    platinum_price = models.IntegerField(default=0)
    gold_price = models.IntegerField(default=0)
    silver_price = models.IntegerField(default=0)
    last_date=models.DateField(default=timezone.now)
    image = models.FileField(upload_to='home/movies/')
    timestamp=models.DateField(default=timezone.now )

    class Meta:
        unique_together = ('slug','name')
        verbose_name='movie'
        verbose_name_plural='movies'
        

    def __str__(self):
        return self.name

class Booking(models.Model):
    visitor_name=models.CharField(max_length=200,default='')
    phone_number=models.IntegerField(default=0)
    event_name=models.CharField(max_length=200,default='')
    platinum_seats = models.IntegerField(default=0)
    gold_seats = models.IntegerField(default=0)
    silver_seats = models.IntegerField(default=0)
    time_choice=(
        ('Moring 9-12','Moring 9-12'),
        ('12-3 ','12-3'),
        ('3-6','3-6'),
        ('6-9','6-9'),
        ('night 9-12','night 9-12'),
    )

    time_preference=models.CharField(max_length=20,choices=time_choice,default=0)
    booking_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.visitor_name


# class BookinValidation(models.Model):
#     visitor_name=models.CharField(max_length=200,default='')
#     phone_number = models.IntegerField(default=0)
#     time_preference = models.CharField(max_length=10, default=0)
#     platinum_seats = models.IntegerField(default=0)
#     gold_seats = models.IntegerField(default=0)
#     silver_seats = models.IntegerField(default=0)
#     booked_date=models.DateField(default=timezone.now)
#
#     def __str__(self):
#         return self.visitor_name
#
#
