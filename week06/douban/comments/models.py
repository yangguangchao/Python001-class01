from django.db import models

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie_name = models.CharField(max_length=128）
    rating_star = models.IntegerField()
    comment_info = models.CharField(max_length=6000)

    class Meta:
        managed = False
        db_table = 'movie_comments'
