import os

m2km = 0.001
km2m = 1000
cm2dm = 0.1
dm2cm = 10
mm2cm = 0.1
cm2mm = 10
dm2m = 0.1
m2dm = 10
mm2m = 0.001
m2mm = 1000
mm2km = 0.000001
km2mm = 1000000
mm2dm = 0.1
dm2mm = 100
cm2m = 0.01
m2cm = 100
km2cm = 100000
cm2km = 0.00001
dm2km = 0.001
km2dm = 10000
cm2dm = 0.1
dm2cm = 10

conversion_factors = {
    ('m', 'km'): m2km,
    ('km', 'm'): km2m,
    ('cm', 'dm'): cm2dm,
    ('dm', 'cm'): dm2cm,
    ('mm', 'cm'): mm2cm,
    ('cm', 'mm'): cm2mm,
    ('dm', 'm'): dm2m,
    ('m', 'dm'): m2dm,
    ('mm', 'm'): mm2m,
    ('m', 'mm'): m2mm,
    ('mm', 'km'): mm2km,
    ('km', 'mm'): km2mm,
    ('mm', 'dm'): mm2dm,
    ('dm', 'mm'): dm2mm,
    ('cm', 'm'): cm2m,
    ('m', 'cm'): m2cm,
    ('km', 'cm'): km2cm,
    ('cm', 'km'): cm2km,
    ('dm', 'km'): dm2km,
    ('km', 'dm'): km2dm,
    ('cm', 'dm'): cm2dm,
    ('dm', 'cm'): dm2cm,
    ('m', 'm'): 1,
    ('km', 'km'): 1,
    ('cm', 'cm'): 1,
    ('dm', 'dm'): 1,
    ('mm', 'mm'): 1
}

i1 = input("Select any input unit (metric mm-km): ")
i2 = input("Select desired output unit (metric mm-km): ")
value = float(input("Enter the value to convert: "))

if (i1, i2) in conversion_factors:
    result = value * conversion_factors[(i1, i2)]
    print(f"{value} {i1} is {result} {i2}")
else:
    print("Conversion not supported.")