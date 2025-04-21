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


class LostItem(models.Model):
    L_ID = models.AutoField(primary_key=True)
    L_Description = models.TextField()
    L_PublishDate = models.CharField(max_length=10)  # mm/dd/yyyy
    L_information = models.TextField()
    U_ID = models.IntegerField()
    L_Photo = models.BinaryField(null=True, blank=True)  # For LONGBLOB

    class Meta:
        db_table = 'LostItems'
        managed = False  # Table already exists in MySQL