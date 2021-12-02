from django.http import HttpResponse
from django.core import serializers
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
import json
from necktieapp.models import Contact
from necktieapp.models import Doctor
from necktieapp.doctorgenerator import DoctorGenerator

# Create your views here.

def index(request):
    return HttpResponseRedirect('/doctor')

def get_all_doctors(request):
    if request.method != 'GET':
        emptyResponse = json.dumps([{}])
        return HttpResponse(emptyResponse, content_type='text/json')

    data = {}
    for doctor in Doctor.objects.all():
        data[doctor.id] = getDoctorJson(doctor)

    return HttpResponse(json.dumps(data), content_type='text/json')
    
def getContacts(doctorId):
    contacts = Contact.objects.filter(doctor = doctorId)
    return ', '.join(str(x.number) for x in contacts)

def getDoctorJson(doctor):
    doctorJson = {
            "name" : doctor.name,
            "category" : doctor.category,
            "address" : doctor.address.street + " " + doctor.address.city,
            "contacts" : getContacts(doctor.id),
            "fee" : {
                "price" : str(doctor.fee.price),
                "daysIncludingMedicine" : doctor.fee.daysIncludingWesternMeds
            }
        }
    return doctorJson
 

def generate_doctor_data(request):
    Doctor.objects.all().delete()

    generator = DoctorGenerator()
    generator.generate()

    return HttpResponseRedirect('/doctor')
