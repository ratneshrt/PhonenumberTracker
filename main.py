import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("Enter your phone number with country code: ")

ch_no = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_no, "en"))

ser_no = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(ser_no, "en"))
