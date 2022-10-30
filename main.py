#  program;Calculate Celone Electricityboard Bill Amount for Domestic Users
#  athor;harindu adhikari
#  date;10/30/2022

Balunits = 0
S1units = 30
S2units = 30
S3units = 30
S4units = 90
S1rate = 16
S2rate = 16
S3rate = 16
S4rate = 50
AboveS4rate = 75
S1Tot = 0
S2Tot = 0
S3Tot = 0
S4Tot = 0
AboveS4Tot = 0
TotAmt = 0
S1Fixedrate = 0
S2Fixedrate = 360
S3Fixedrate = 960
S4Fixedrate = 960
AboveS4Fixedrate = 1500
units = input("Input your Monthley units: ")
Balunits = units
if (int(Balunits) <= int(S1units)):
    S1Tot = (int(Balunits) * int(S1units))
    S1Tot = (int(S1Tot) + int(S1Fixedrate))
    print("slab1 total", int(S1Tot))
else:
    S1Tot = (int(S1units) * int(S1rate))
    Balunits = (int(Balunits) - int(S1units))
    print("slab1 total", int(S1Tot))
    if (int(Balunits) <= int(S2units)):
        S2Tot = (int(Balunits) * int(S2units))
        S2Tot = (int(S2Tot) + int(S2Fixedrate))
        print("slab2 total", int(S2Tot))
    else:
        S2Tot = (int(S2units) * int(S2rate))
        Balunits = (int(Balunits) - int(S2units))
        print("slab2 total", int(S2Tot))
        if (int(Balunits) <= int(S3units)):
            S3Tot = (int(Balunits) * int(S3units))
            S3Tot = (int(S3Tot) + int(S3Fixedrate))
            print("slab3 total", int(S3Tot))
        else:
            S3Tot = (int(S3units) * int(S3rate))
            Balunits = (int(Balunits) - int(S3units))
            print("slab3 total", int(S3Tot))
            if (int(Balunits) <= int(S4units)):
                S4Tot = (int(Balunits) * int(S4units))
                S4Tot = (int(S4Tot) + int(S4Fixedrate))
                print("slab4 total", int(S4Tot))
            else:
                S4Tot = (int(S4units) * int(S4rate))
                Balunits = (int(Balunits) - int(S4units))
                AboveS4Tot = (int(Balunits) * int(AboveS4rate))
                AboveS4Tot = (int(AboveS4Tot) + int(AboveS4Fixedrate))
                print("slab4 total", int(S4Tot))
            TotAmt = (int(S1Tot) + int(S2Tot) + int(S3Tot) + int(S4Tot) + int(AboveS4Tot))
            print("TotAmt", TotAmt)
