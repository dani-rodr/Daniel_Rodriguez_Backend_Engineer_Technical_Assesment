from necktieapp.specialization import Specialization
from necktieapp.models import Address
from necktieapp.models import Fee
from necktieapp.models import Contact
from necktieapp.models import Doctor

import random
import names
import random_address

class DoctorGenerator:
    
    def generateRandomFee(self):
        price = random.randrange(100, 1000, 10)
        dayWithFreeMeds = random.randint(0, 7)
        fee = Fee(price = price, daysIncludingWesternMeds = dayWithFreeMeds)
        fee.save()
        return fee

    def generateContact(self, doctor):
        numOfContacts = random.randint(1, 3)
        contacts = []
        for x in range(numOfContacts):
            contact = Contact(doctor = doctor, number = random.randint(10000000, 99999999))
            contact.save()
            contacts.append(contact)
        return contacts

    def generateAddress(self):
        randomAddress = (random_address.real_random_address())
        address =  Address(street = randomAddress.get('address1'), city = randomAddress.get('city'))
        address.save()
        return address

    def generateCategory(self):
        categories = Specialization()._categories
        index  = random.randint(0, len(categories) - 1)
        return categories[index]

    def generate(self):
        for x in range(50):
            name = names.get_full_name()
            fee = self.generateRandomFee()
            address = self.generateAddress()
            category = self.generateCategory()

            doctor = Doctor(name = name, fee = fee,
                            address = address, category = category)
            doctor.save()
            contacts = self.generateContact(doctor)