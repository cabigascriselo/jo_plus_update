from django import forms
from .models import Equipment, EquipmentParts, Job_Order

#Create forms
class EquipmentForm(forms.ModelForm):
 class Meta:
  model = Equipment
  fields = ['equipment']
  labels = {'equipment': 'Equipment'}


class PartsForm(forms.ModelForm):
 class Meta:
  model = EquipmentParts
  fields = ['parts']
  labels = {'parts': 'Parts'}


class JobOrderForm(forms.ModelForm):
 class Meta:
  model = Job_Order
  fields = [
    'issued_to', 'location', 'process', 'equipment', 'parts', 'service_type', 'requestor',
    'complaint', 'department', 'approver',  'status'
   ]
  labels = {
    'issued_to': 'Issued to: ', 'location': 'Location: ', 'process': 'Process: ', 
    'equipment': 'Equipment: ', 'parts': 'Parts: ', 'service_type': 'Service Type', 
    'requestor': 'Requestor: ', 'complaint': 'Complaint', 'department': 'Department',
    'approver': 'Approver: ', 'status': 'Open: '
  }


class CloseForm(forms.ModelForm):
 class Meta:
  model = Job_Order
  fields = ['status']
  labels = {'status': 'Uncheck to closed:'}
  