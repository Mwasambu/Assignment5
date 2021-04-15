print("Options:")
print("[P] Print Options")
print("[C] Convert from Celsius")
print("[F] Convert from Fahrenheit")
print("[M] Convert from Miles")
print("[KM] Convert from Kilometers")
print("[IN] Convert from Inches")
print("[CM] Convert from Centimeters")
print("[Q] Quit ")

ChoiceMade = True

def Conversion():
    option = str.upper(input("Option:"))
    if option=='C':
        CelTemp = float(input("Celcius Temperature: "))
        FahrenheitTemp = ((CelTemp * 9 / 5) + 32)
        print("Fahrenheit: " + str(FahrenheitTemp))
    elif option=='F':
        FahrenheitTemp = float(input("Fahrenheit Temperature: "))
        CelTemp = ((FahrenheitTemp - 32) * (5 / 9))
        print("Celcius: " + str(CelTemp))
    elif option=='M':
        miles=float(input("Distance in Miles: "))
        kms=miles*1.60934
        print("Distance in Kilometers: " + str(kms))
    elif option=='KM':
        kms = float(input("Distance in Kilometers: "))
        miles = kms / 1.60934
        print("Distance in Miles: " + str(miles))
    elif option=='IN':
        Inc=float(input("Length in Inches: "))
        Cm=Inc*2.54
        print("Lenght in Centimetes: " + str(Cm))
    elif option=='CM':
        Cm=float(input("Length in Centimeters: "))
        Inc=Cm/2.54
        print("Lenght in Inches: " + str(Inc))
    elif option =='Q':
        exit()
    else:
        print("WRONG CHOICE. PLEASE, TRY AGAIN")
        ChoiceMade = False
#call Function Conversion
while ChoiceMade==True:
    Conversion()
