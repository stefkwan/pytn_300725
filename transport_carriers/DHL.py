companyName = "DHL Australia"
companyABN = "3145556785"
companyEmail = "dhl_sales_australia@dhl.com"
companyPhone = "02-96754567"
contactPerson = "Christopher Galea"
companyAddress = "324 Market Street, North Sydney, NSW 2000"
companyWebsite = "www.dhl.com/au"


def pricing(weight_kg,height_cm,length_cm,width_cm):
    cubic_metric = height_cm * length_cm * width_cm
    price_per_metric = 5
    price_per_kg = 0.5
    print ((cubic_metric* price_per_metric) + (weight_kg*price_per_kg))

print("DHL.py inported")
