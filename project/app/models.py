
from django.db import models


class AadharModel(models.Model):
    aadhar_no=models.IntegerField()
    def _str_(self):
        return str(self.aadhar_no)

class StudentModel(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_address = models.CharField(max_length=200)  
    # CASCADE - Means if we delete aadhar_no then related StudentModel also deleted.
    aadhar_no = models.OneToOneField(AadharModel,on_delete=models.CASCADE,primary_key=True)
    
    # PROTECT - Means if you want delet aadhar no then it is require to delete first alloted student name.
    # aadhar_no = models.OneToOneField(AadharModel, on_delete=models.PROTECT,primary_key=True)
    def _str_(self):
        return self.stu_name