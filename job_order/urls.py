from django.urls import path

from . import views

app_name = 'job_order'


urlpatterns = [
 path('', views.index, name='index'),
 path('my_main/', views.my_main, name='my_main'),
 path('locations/', views.locations, name='locations'),
 path('locations/<int:location_id>/', views.location, name='location'),
 path('processes/<int:process_id>/', views.process, name='process'),
 path('add_equipment/<int:process_id>/', views.add_equipment, name='add_equipment'),
 path('add_parts/<int:equipment_id>/', views.add_parts, name='add_parts'),
 path('equipments/<int:equipment_id>/', views.equipment, name='equipment'),
 path('parts/', views.parts, name='parts'),
 path('parts/<int:part_id>/', views.part, name='part'),
 path('equipments/', views.equipments, name='equipments'),
 path('jo_lists/', views.jo_lists, name='jo_lists'),
 path('jo_lists/<int:jo_list_id>/', views.jo_list, name='jo_list'),
 path('create_jo/', views.create_jo, name='create_jo'),
 path('edit_jo/<int:job_order_id>/', views.edit_jo, name='edit_jo'),
 path('edit_equipment/<int:equipment_id>/', views.edit_equipment, name='edit_equipment'),
 path('edit_parts/<int:part_id>/', views.edit_parts, name='edit_parts'),
 path('details/<int:detail_id>/', views.detail, name='detail'),
 path('file_pdf/<int:file_id>/', views.generate_Filepdf, name='generate_Filepdf'),
 path('pdf_report/', views.pdf_report, name='pdf_report'),
 path('export_jo_to_excel/', views.jo_excel, name='jo_excel'),
 path('time_diff/', views.time_diff, name='time_diff'),
 path('starter/', views.starter, name='starter'),
 path('close_jo', views.close_jo, name='close_jo'),
 path('disabled_register/', views.disabled_register, name='disabled_register'),
 path('supervisor_list', views.supervisor_list, name='supervisor_list'),
]