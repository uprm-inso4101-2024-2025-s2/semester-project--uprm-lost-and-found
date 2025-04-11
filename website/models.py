from django.db import models

class User(models.Model):
    U_ID = models.AutoField(primary_key=True)
    U_Username = models.CharField(max_length=20, unique=True)
    U_Email = models.CharField(max_length=30, unique=True)
    U_Password = models.CharField(max_length=128)  # you should hash it
    U_ProfilePhoto = models.BinaryField(null=True)

    class Meta:
        db_table = 'Users'