from unit_conversions import *

print("This is a tool that will allow you to convert measurements.")
type_of_conversion = input("What Type of Unit Conversion Will You Do (Length, Volume, Mass): ")

while type_of_conversion.lower() != "length" or type_of_conversion != "volume" or type_of_conversion != "mass":
    print("Invalid Function.")
    type_of_conversion = input("What Type of Unit Conversion Will You Do (Length, Volume, Mass): ")

if type_of_conversion.lower() == "length":
    init_unit = input("What Is The Initial Unit You Will Use (cm, in, ft, yd, mm, m, mi, km): ")
    while init_unit not in {"cm", "in", "ft", "yd", "mm", "m", "mi", "km"}:
        print("Invalid Unit.")
        init_unit = input("What Is The Initial Unit You Will Use (cm, in, ft, yd, mm, m, mi, km): ")