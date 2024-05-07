from django.shortcuts import render
from django.http import HttpResponse
from . models import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactform(request):
    if request.method == "POST":
        nam = request.POST.get("c_name")
        em = request.POST.get("c_email")
        sub = request.POST.get("c_subject")
        msg = request.POST.get("c_message")
        abc = ContactForm(name=nam, email=em, subject=sub, message=msg)
        abc.save()
        return HttpResponse("<h4>DATA SENT SUCCESSFULLY</h4>")
    else:
        return render(request,'index.html')