from django.db import models

# Create your models here.
class MobilePhone(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    sentiments = models.DecimalField(max_digits=11,decimal_places = 10)
    comment = models.CharField(max_length = 512)
    comment_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mobile_phone_sentiments'