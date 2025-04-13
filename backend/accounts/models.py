from django.db import models

class User(models.Model):
    U_ID = models.AutoField(primary_key=True)
    U_Username = models.CharField(max_length=20)
    U_FullName = models.CharField(max_length=50)
    U_Email = models.EmailField(max_length=30, unique=True)
    U_Password = models.CharField(max_length=20)
    U_Occupation = models.CharField(max_length=20)
    U_ProfilePhoto = models.BinaryField(null=True, blank=True)
    class Meta:
        db_table = 'Users'