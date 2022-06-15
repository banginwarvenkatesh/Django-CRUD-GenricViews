from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import LandRec
from django.urls import reverse_lazy


class ListLand(ListView):
    model = LandRec
    fields = "__all__"
    paginate_by = 2

class CreateLand(CreateView):
    model = LandRec
    fields = "__all__"
    template_name = 'landrecord/landrec_form.html'
    success_url = reverse_lazy('list_url')

class DeleteLand(DeleteView):
    model = LandRec
    fields = "__all__"
    success_url = reverse_lazy('list_url')

class UpdateLand(UpdateView):
    model = LandRec
    fields = "__all__"
    success_url = reverse_lazy('list_url')
    
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def GenPDF(request):
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica', 14)
    lines =[]
    farm = LandRec.objects.all()

    for f in farm:
        lines.append(f.farmer_name)
        lines.append(f.survey_number)
        lines.append(f.village)
        lines.append(f.farm_area)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='xyz.pdf')

def IndPDF(request,pk):
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica', 14)
    lines = []
    farm = LandRec.objects.get(id=pk)
    nm = farm.farmer_name
    sn = farm.survey_number
    vil = farm.village
    ar= farm.farm_area
    #im = farm.framer_image
    d={"FARMER NAME:":nm, "SURVEY NUMBER:":sn,
        "VILLAGE:":vil, "FARM AREA:":ar  
    }

    for k,v in d.items():
        lines.extend([k,v," "])

    for line in lines:
        textob.textLine(line)
    
    c.setFillColor(colors.darkorchid)
    c.drawCentredString(270,30, "LAND RECORD")
    c.line(30,50, 570,50)
    c.setFillColor(colors.greenyellow)
    #c.drawImage(90,480,'./media/images/men_pp_nTM2qsk.jpg')
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'{nm}.pdf')




# Create your views here.
