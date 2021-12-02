from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from necktieapp.models import *
from necktieapp.doctorgenerator import DoctorGenerator

# Create your views here.

def index(request):
    return HttpResponseRedirect('/doctor')

def get_all_doctors(request):
    data = {}

    category = request.GET.get('category')
    district = request.GET.get('district')
    min = request.GET.get('min')
    max = request.GET.get('max')
    filter = Q()
    if (category):
        filter |= Q(category = category)

    for doctor in Doctor.objects.all().select_related('address').filter(filter):
        data[doctor.id] = getDoctorJson(doctor)

    return HttpResponse(json.dumps(data), content_type='text/json')

def get_doctor(request, id):

    if not Doctor.objects.filter(id = id).exists():
        return HttpResponse(json.dumps({'error': 'id {} not found'.format(id)}), content_type='text/json')

    data = {}
    doctor = Doctor.objects.get(id = id)
    data[id] = getDoctorJson(doctor)

    return HttpResponse(json.dumps(data), content_type='text/json')

@csrf_exempt
def add_doctor(request):
    data = json.loads(request.body)
    address = Address(street = data['address']['street'], city = data['address']['city'])
    address.save()
    fee = Fee(price = data['fee']['price'], daysIncludingWesternMeds = data['fee']['daysIncludingMedicine'])
    fee.save()
    doctor = Doctor(name = data['name'], category = data['category'],
                    address = address, fee = fee)
    doctor.save()
    setContacts(data['contacts'], doctor)

    return HttpResponseRedirect('/doctor/{}'.format(doctor.id))

def setContacts(contactString, doctor):
    contactStrs = contactString.split(',')
    contacts = []
    for contactStr in contactStrs:
        contact = Contact(number = int(contactStr), doctor = doctor)
        contact.save()
        contacts.append(contact)
    return contacts
    
def getContacts(doctorId):
    contacts = Contact.objects.filter(doctor = doctorId)
    return ', '.join(str(x.number) for x in contacts)

def getDoctorJson(doctor):
    doctorJson = {
            "name" : doctor.name,
            "category" : doctor.category,
            "address" : {
                "street" : doctor.address.street,
                "city" : doctor.address.city
            },
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
