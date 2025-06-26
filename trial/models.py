from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class content(models.Model):
   TRIAL_TYPE_CHOICE = [
      ('F','FREE'),('B','BASIC'),('S','STANDARD'),('P','PREMIUM'),('PP','PREMIUM PLUS')
   ]
   name = models.CharField(max_length=100)
   image = models.ImageField(upload_to='image/')
   date_added = models.DateTimeField(default=timezone.now)
   type = models.CharField(choices=TRIAL_TYPE_CHOICE)
   description = models.TextField(default='')
   def __str__(self):
       return self.name

class TrialReview(models.Model):
   trial = models.ForeignKey(content, on_delete=models.CASCADE, related_name='reviews')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   rating = models.IntegerField()
   comment = models.TextField()
   date_added = models.DateTimeField(default=timezone.now)
   def __str__(self):
       return f'{self.user.username} review for {self.trial.name}'

class Store(models.Model):
   name = models.CharField(max_length=100)
   contents = models.ManyToManyField(content, related_name='stores')
   def __str__(self):
       return self.name
    
class trialcertificate(models.Model):
   trial = models.OneToOneField(content, related_name='certificate', on_delete=models.CASCADE)
   certificate_number = models.CharField(max_length=100)
   issued_date = models.DateTimeField(default = timezone.now)
   valid_until = models.DateTimeField()
   def __str__(self):
       return self.name

