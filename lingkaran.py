pi = 3.14


def area_lingkaran(r=7):
    print("Area:", r * r * pi)


def diameter_lingkaran(r=7):
    print("Diameter:", 2 * pi * r)


print("hello saya lingkaran.py")

text = ""
while (text != "exit"):
    text = input("Enter radius")
    r = float(text)

    area_lingkaran(r)
    diameter_lingkaran(r)
