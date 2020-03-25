from django.db import models

class JobOffert(models.Model):
    title = models.CharField(max_length=256)
    price_range = models.CharField(max_length=128)
    company = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    keywords = models.CharField(max_length=256)
    job_service = models.CharField(default="JustJoinIT", max_length=128)

    def __str__(self):
        return f'{self.title}, {self.company}'

    class Meta:
        verbose_name = 'job offert JJIT'