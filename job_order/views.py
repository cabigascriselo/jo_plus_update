from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import (Location, Process, Equipment, EquipmentParts, Job_Order)
from .forms import (EquipmentForm, PartsForm, JobOrderForm, CloseForm)
import pandas as pd
from datetime import datetime, timezone
from django.db.models import Prefetch

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


#Create your views here.

def index(request):
    return render(request, 'job_order/index.html')


@login_required
def my_main(request):
    return render(request, 'job_order/my_main.html')


@login_required
def locations(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'job_order/locations.html', context)


def location(request, location_id):
    location = Location.objects.get(id=location_id)
    processes = location.processes.all()
    context = {'processes': processes, 'location': location}
    return render(request, 'job_order/location.html', context)


def process(request, process_id):
    process = Process.objects.get(id=process_id)
    machines = process.machines.all()
    context = {'process': process, 'machines': machines}
    return render(request, 'job_order/process.html', context)


@login_required
def add_equipment(request, process_id):
    """Add equipment to a particular process"""
    process = Process.objects.get(id=process_id)
    if request.method != 'POST':
    #No data submitted, create a blank form
        form = EquipmentForm()
    else:
    #POST data submitted, process data
        form = EquipmentForm(data=request.POST)
        if form.is_valid():
            add_equipment = form.save(commit=False)
            add_equipment.process = process
            add_equipment.save()
            return redirect('job_order:process', process_id=process_id)

    #Display blank or invalid form
    context = {'form': form, 'process': process}
    return render(request, 'job_order/add_equipment.html', context)


@login_required
def add_parts(request, equipment_id):
    """Add parts to the equipment"""
    #No data submitted, create blank form
    equipment = Equipment.objects.get(id=equipment_id) 
    if request.method != 'POST':
        form = PartsForm()
    else:
        #POST data submitted, process data
        form = PartsForm(data=request.POST)
    if form.is_valid():
        add_parts = form.save(commit=False)
        add_parts.equipment = equipment
        add_parts.save()
        return redirect('job_order:equipment', equipment_id=equipment_id)

    #Display blank or invalid form
    context = {'equipment': equipment, 'form': form}
    return render(request, 'job_order/add_parts.html', context)


def parts(request):
    parts = EquipmentParts.objects.all()
    context = {'parts': parts}
    return render(request, 'job_order/parts.html', context)


def part(request, part_id):
    part = EquipmentParts.objects.get(id=part_id)
    parts_lists = part.parts_lists.all()
    context = {'part': part, 'parts_lists': parts_lists}
    return render(request, 'job_order/part.html', context)


def equipments(request):
    equipments = Equipment.objects.all()
    context = {'equipments': equipments}
    return render(request, 'job_order/equipments.html', context) 


def equipment(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    job_order = equipment.machine_unit.all()
    specifications = equipment.specifications.all()
    spare_parts = equipment.spare_parts.all()
    context = {
        'specifications': specifications, 
        'spare_parts': spare_parts, 
        'equipment': equipment, 
        'job_order': job_order
        }
    return render(request, 'job_order/equipment.html', context)


def jo_lists(request):
    jo_lists = Job_Order.objects.filter(status=True)
    for jo_list in jo_lists:
        jo_list.date = jo_list.date.strftime("%m/%d/%Y")
    
    close_lists = Job_Order.objects.filter(status=False)
    for close_list in close_lists:
        close_list.date = close_list.date.strftime("%m/%d/%Y")
    context = {'jo_lists': jo_lists, 'close_lists': close_lists}
    return render(request, 'job_order/jo_lists.html', context)


def supervisor_list(request):
    #jo_lists = Job_Order.objects.filter(owner=request.user)
    jo_lists = Job_Order.objects.filter(status=True)
    for jo_list in jo_lists:
        jo_list.date = jo_list.date.strftime("%m/%d/%Y")
    
    close_lists = Job_Order.objects.filter(status=False)
    for close_list in close_lists:
        close_list.date = close_list.date.strftime("%m/%d/%Y")
    
    context = {'jo_lists': jo_lists, 'close_lists': close_lists}
    return render(request, 'job_order/supervisor_list.html', context)


@login_required
def create_jo(request):
    """Create job order"""
    #No data submitted, create a blank form
    if request.method != 'POST':
        form = JobOrderForm()
    else:
    #POST data submitted, process data
        form = JobOrderForm(data=request.POST) 
    if form.is_valid():
        form.save()
        return redirect('job_order:supervisor_list') 

    #Display blank or invalid form
    context = {'form': form}
    return render(request, 'job_order/create_jo.html', context)


@login_required
def edit_jo(request, job_order_id):
    """Edit existing job order"""
    job_order = Job_Order.objects.get(id=job_order_id) 

    if request.method != 'POST':
        #Initial request: prefill form with current jo entry
        form = JobOrderForm(instance=job_order)
    else:
        #POST data submitted, process data
        form = JobOrderForm(instance=job_order, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('job_order:jo_lists') 

    context = {'job_order': job_order, 'form': form}
    return render(request, 'job_order/edit_jo.html', context)


def jo_list(request, jo_list_id):
    jo_list = Job_Order.objects.get(id=jo_list_id)
    if jo_list.date:
        jo_list.date = jo_list.date.strftime("%m/%d/%Y")
    context = {'jo_list': jo_list}
    return render(request, 'job_order/jo_list.html', context) 


@login_required
def edit_equipment(request, equipment_id):
    """Edit equipment"""
    equipment = Equipment.objects.get(id=equipment_id)
    process = equipment.process

    if request.method != 'POST':
        #Initial request, pre-fill the form with the current data
        form = EquipmentForm(instance=equipment)
    else:
        #POST data submitted, process data
        form = EquipmentForm(instance=equipment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_order:equipment', equipment_id=equipment.id)
    
    context = {'form': form, 'equipment': equipment, 'process': process}
    return render(request, 'job_order/edit_equipment.html', context)


@login_required
def edit_parts(request, part_id):
    """Edit parts"""
    part = EquipmentParts.objects.get(id=part_id)
    equipment = part.equipment

    if request.method != 'POST':
        #Initial request, pre-fill the form with current data...
        form = PartsForm(instance=part)
    else:
        #POST data submitted, process data
        form = PartsForm(instance=part, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_order:part', part_id=part.id)
    
    context = {'part': part, 'equipment': equipment, 'form': form}
    return render(request, 'job_order/edit_parts.html', context)


@login_required
def detail(request, detail_id):
    detail = Job_Order.objects.get(id=detail_id)
    context = {'detail': detail}
    return render(request, 'job_order/details.html', context)


@login_required
def pdf_report(request):
    pdf_reports = Job_Order.objects.all()
    for pdf_report in pdf_reports:
        pdf_report.date = pdf_report.date.strftime("%m/%d/%Y")
    context = {'pdf_reports': pdf_reports}
    return render(request, 'job_order/pdf_report.html', context)


@login_required
def generate_Filepdf(request, file_id):
    
    from io import BytesIO
    from PIL import Image

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    
    # Create a PDF document
    jo = Job_Order.objects.get(id=file_id)
    
    # define a large font
    p.setFont("Helvetica", 20)
    p.drawString(270, 800, "JOB ORDER REQUEST - CES")
 
    p.rect(x=230, y=780, width=355, height=50, stroke=1, fill=0)
    p.rect(x=15, y=780, width=215, height=50, stroke=1, fill=0) 
 
    y = 775
    p.setFont("Helvetica", 12)
    p.drawString(20, y - 20, f"Job Order ID: {jo.id}")
    date_convert = jo.date.strftime("%m/%d/%Y")
    p.drawString(350, y - 20, f"Date: {date_convert}")
    p.drawString(20, y - 40, f"Issued To: {jo.issued_to}")
    p.drawString(350, y - 40, f"Dept.: {jo.department}")
    p.drawString(20, y - 60, f"Location: {jo.location}")
    p.drawString(350, y - 60, f"System: {jo.process}")
    p.drawString(20, y - 80, f"Equipment: {jo.equipment}")
    p.drawString(350, y - 80, f"Part name: {jo.parts}")
    p.drawString(20, y - 100, f"Complaint:")
    p.rect(x=15, y=600, width=570, height=70, stroke=1, fill=0)
    p.drawString(25, y - 120, f"{jo.complaint}")
    p.drawString(20, y - 190, f"Service type: {jo.service_type}")
    p.drawString(350, y - 190, f"Received by (PMD/EID):")
    p.drawString(20, y - 230, f"Requested by: {jo.requestor}")
    p.drawString(350, y - 230, f"Opt. Asst./Planner/S'visor:______________")
    p.drawString(20, y - 265, f"Approved by: {jo.approver}")
    p.drawString(350, y - 265, f"Approved by (Dept. Head):_____________")
    x_start = 0
    y_start = 0
    #image = Image.open('abi_logo.jpeg')
    p.drawImage('abi_logo.png', 25, 782, width=195, height=45)
    p.line(x1=20, y1=500, x2=570, y2=500)
    p.setFont("Helvetica", 8)
    p.drawString(350, y - 285, f"DOC. NO.: ABI2-UTL-L4-110 REV00 EFF12152024")
    p.showPage()
    p.save()
 
    buffer.seek(0)

    response = FileResponse( 
        buffer, 
        as_attachment=True, 
        filename='jo_pdf.pdf')
    return response


@login_required
def jo_excel(request):
    # Query the Job Order model to get all records
 
    jo_excel = Job_Order.objects.all().prefetch_related('equipment').values()
    
    # Convert the QuerySet to a DataFrame
    df = pd.DataFrame(list(jo_excel))
    df['date'] = pd.to_datetime(df['date'])

    # Remove timezone information
    df['date'] = df['date'].dt.tz_localize(None)
    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=job_order.xlsx'

    # Use Pandas to write the DataFrame to an Excel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response


def time_diff(request):
    jo_lists = Job_Order.objects.filter(status=True)
    now = datetime.now()
    lead_times = []
    #df = pd.DataFrame(jo_lists)
    for jo_list in jo_lists:
        if jo_list.date:
            start = jo_list.date.replace(tzinfo=None)
            jo_list.date = jo_list.date.strftime("%m/%d/%Y")
            lead = (now-start).days
            jo_list.lead_times = lead
   
    #context = { 'datas': df.to_html(), 'jo_lists': jo_lists }
    context = {'lead_times': lead_times, 'jo_lists': jo_lists}
    return render(request, 'job_order/time_diff.html', context)


def starter(request):
    xy = {}
    keysList = []
    valueList = []
    job_orders = Job_Order.objects.filter(status=True)
   
    x_duplicate = [x_duplicate.equipment for x_duplicate in job_orders]
    x_single = list(set(x_duplicate))
    for x in x_single:
        xy[x] = x_duplicate.count(x)

    xy_sort = {k: v for k, v in sorted(xy.items(), key=lambda item: item[1], reverse=True)}
    for key_val in xy_sort.keys():
        keysList.append(key_val)
    for val in xy_sort.values():
        valueList.append(val)


    context = {'keysList': keysList, 'valueList': valueList, 'xy_sort': xy_sort}


    return render(request, 'job_order/starter.html', context)



def close_jo(request):
    """close job order"""
    jo_close = Job_Order.objects.filter(status=False) 

    context = {'jo_close': jo_close}
    return render(request, 'job_order/close_jo.html', context)



def disabled_register(request):
    """Pop up message"""
    return HttpResponse('DISABLED REGISTER PAGE')
