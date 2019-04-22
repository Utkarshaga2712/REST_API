from django.db import models

# Create your models here.
class peoples(models.Model):
    userName=models.CharField(max_length=25)
    emailid=models.EmailField(max_length=50)
    phoneNo=models.IntegerField()
    password=models.CharField(max_length=50)
 #   datetime=models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "userData"
