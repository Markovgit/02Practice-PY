import phonenumbers 
from phonenumbers import geocoder ,carrier,timezone

phone = input("Enter  a phone number: ")
phone_number = phonenumbers.parse(phone)

#how to know the country name 
country_name = geocoder.description_for_number(phone_number,'en')


service_provider = carrier.name_for_number(phone_number, 'en')

time_zone = timezone.time_zones_for_geographical_number(phone_number)


#print(f"The service provider is {service_provider}")
print("Country Name:",country_name)
print("Service Provider:",service_provider)
print("Time Zone:",time_zone)