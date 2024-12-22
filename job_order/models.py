from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
# Create your models here.
class Location(models.Model):
 location = models.CharField(max_length=64)

 def __str__(self):
  return f'{self.location}'


class Process(models.Model):
 process = models.CharField(max_length=64)
 location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='processes')

 def __str__(self):
  return f'{self.process}'


class Equipment(models.Model):
 equipment = models.CharField(max_length=64)
 process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='machines')

 def __str__(self):
  return f'{self.equipment}'


class EquipmentSpecs(models.Model):
 specs = models.TextField() 
 equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='specifications')

 def __str__(self):
  return f'{self.specs}'


class EquipmentParts(models.Model):
 parts = models.CharField(max_length=64)
 equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='spare_parts')

 def __str__(self):
  return f'{self.parts}' 


class Requestor(models.Model):
 name = models.CharField(max_length=64)

 def __str__(self):
  return f"{self.name}"


class Issued_To(models.Model):
 jo_issued_to = models.CharField(max_length=64)

 def __str__(self):
  return f"{self.jo_issued_to}"


class Approver(models.Model):
 approver = models.CharField(max_length=64)

 def __str__(self):
  return f"{self.approver}"


class Service_Type(models.Model):
 service = models.CharField(max_length=64)

 def __str__(self):
  return f"{self.service}"


class Department(models.Model):
 department = models.CharField(max_length=64)

 def __str__(self):
  return f"{self.department}"


class Job_Order(models.Model):
 date = models.DateTimeField(auto_now_add=True)
 issued_to = models.ForeignKey(Issued_To, on_delete=models.CASCADE, related_name='assigned_to')
 location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='area_located')
 process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='systems')
 equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='machine_unit')
 parts = models.ForeignKey(EquipmentParts, on_delete=models.CASCADE, related_name='parts_lists')
 service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE, related_name='job_type')
 requestor = models.ForeignKey(Requestor, on_delete=models.CASCADE, related_name='requested_by')
 complaint = models.TextField()
 department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept')
 approver = models.ForeignKey(Approver, on_delete=models.CASCADE, related_name='approve_by')
 status = models.BooleanField(default=True)
 lead_times = models.IntegerField(default=0)
 owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


 @property
 def jo_issued_to(self):
  return self.issued_to.jo_issued_to

 def __str__(self):
  return f'{self.complaint[0:50]}...'

 
 def save(self, *args, **kwargs):
  super().save(*args, **kwargs)


