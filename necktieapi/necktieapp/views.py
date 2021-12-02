from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.db.models import Q
import json
from necktieapp.models import Contact
from necktieapp.models import Doctor
from necktieapp.doctorgenerator import DoctorGenerator

# Create your views here.

def index(request):
    return HttpResponseRedirect('/doctor')

def get_all_doctors(request):
    data = {}

    category = request.GET.get('category')
    district = request.GET.get('district')
    filter = Q()
    if (category):
        filter |= Q(category = category)
    # if (district):
    #     filter |= Q(city = district)

    for doctor in Doctor.objects.all().filter(filter):
        data[doctor.id] = getDoctorJson(doctor)

    return HttpResponse(json.dumps(data), content_type='text/json')

def get_doctor(request, id):

    if not Doctor.objects.filter(id = id).exists():
        return HttpResponse(json.dumps({'error': 'id {} not found'.format(id)}), content_type='text/json')

    data = {}
    doctor = Doctor.objects.get(id = id)
    data[id] = getDoctorJson(doctor)

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
