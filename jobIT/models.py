from django.db import models
from django.utils import timezone

class JobOffert(models.Model):
    title = models.CharField(max_length=256)
    price_range = models.CharField(max_length=128)
    company = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    keywords = models.CharField(max_length=256)
    job_service = models.CharField(default="JustJoinIT", max_length=128)
    scrappy_date = models.DateField(auto_now_add=True)
    job_url = models.URLField()
    hash_id = models.CharField(max_length=516)
    still_active = models.BooleanField(default=True)
    open_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    #zmienić price range na salary
    def __str__(self):
        return f'{self.title}, {self.company}'

    class Meta:
        verbose_name = 'job offert JJIT'