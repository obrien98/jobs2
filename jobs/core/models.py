from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def create_employer(sender, instance, created, **kwargs):
    if created:
        Employer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employer(sender, instance, **kwargs):
    instance.employer.save()

class Job(models.Model):
    poster = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    establishment_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    details = models.TextField(max_length=2000)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    state_choices = (
        # long list omitted on purpose
    )
    state = models.CharField(choices=state_choices, max_length=20)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.job_title + " - " + self.establishment_name \
               + ", " + self.poster.user.first_name + " " + self.poster.user.last_name


class EmailSubscriber(models.Model):
    email = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

