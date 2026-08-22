from django.db import models

# Create your models here.
class About(models.Model):
    about_head = models.CharField(max_length=50)
    about_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    class Meta:
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.about_head

class SocialLink(models.Model):
    platform_name= models.CharField(max_length=50)
    platform_link= models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.platform_name