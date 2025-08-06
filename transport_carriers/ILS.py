companyName = "International Logistics Services"
companyABN = "5242353757"
companyEmail = "sales@ils.com.au"
companyPhone = "02-94561234"
contactPerson = "Edwin Nguyen"
companyAddress = "1/12 Carribean Street, Crow Nest, NSW 2134"
companyWebsite = "www.ils.com.au"


def pricing(weight_kg,height_cm,length_cm,width_cm):
    cubic_metric = height_cm * length_cm * width_cm
    price_per_metric = 4.5
    price_per_kg = 0.6
    print ((cubic_metric* price_per_metric) + (weight_kg*price_per_kg))

print("ILS.py imported")
