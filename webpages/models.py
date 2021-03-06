from django.db import models

# Create your models here.


class Slider3(models.Model):
    headline  = models.CharField(max_length=255)
    subtitle =  models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    creted_date = models.DateTimeField(auto_now_add=True)
    link_to_btn = models.CharField(max_length=1200)
   

    def __str__(self):
        return self.headline;

class team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    youtube_links = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y")
    cretaed_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name