from django.contrib import admin
from .models import (
 Location, Process, Equipment, EquipmentSpecs, EquipmentParts, Requestor, Issued_To, 
 Approver, Service_Type, Department, Job_Order
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Location)
admin.site.register(Process)
admin.site.register(Equipment)
admin.site.register(EquipmentSpecs)
admin.site.register(EquipmentParts)
admin.site.register(Requestor)
admin.site.register(Issued_To)
admin.site.register(Approver)
admin.site.register(Service_Type)
admin.site.register(Department)
admin.site.register(Job_Order, ImportExportModelAdmin)