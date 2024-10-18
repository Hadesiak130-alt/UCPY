import time

conversion_factors = {
    ('mm', 'mm'): 1,
    ('mm', 'cm'): 0.1,
    ('mm', 'dm'): 0.01,
    ('mm', 'm'): 0.001,
    ('mm', 'km'): 0.000001,
    ('mm', 'in'): 0.0393701,
    ('mm', 'ft'): 0.00328084,
    ('mm', 'yd'): 0.00109361,
    ('mm', 'mi'): 6.2137e-7,

    ('cm', 'mm'): 10,
    ('cm', 'cm'): 1,
    ('cm', 'dm'): 0.1,
    ('cm', 'm'): 0.01,
    ('cm', 'km'): 0.00001,
    ('cm', 'in'): 0.393701,
    ('cm', 'ft'): 0.0328084,
    ('cm', 'yd'): 0.0109361,
    ('cm', 'mi'): 0.0000062137,

    ('dm', 'mm'): 100,
    ('dm', 'cm'): 10,
    ('dm', 'dm'): 1,
    ('dm', 'm'): 0.1,
    ('dm', 'km'): 0.0001,
    ('dm', 'in'): 3.93701,
    ('dm', 'ft'): 0.328084,
    ('dm', 'yd'): 0.109361,
    ('dm', 'mi'): 0.0000621371,

    ('m', 'mm'): 1000,
    ('m', 'cm'): 100,
    ('m', 'dm'): 10,
    ('m', 'm'): 1,
    ('m', 'km'): 0.001,
    ('m', 'in'): 39.3701,
    ('m', 'ft'): 3.28084,
    ('m', 'yd'): 1.09361,
    ('m', 'mi'): 0.000621371,

    ('km', 'mm'): 1000000,
    ('km', 'cm'): 100000,
    ('km', 'dm'): 10000,
    ('km', 'm'): 1000,
    ('km', 'km'): 1,
    ('km', 'in'): 39370.1,
    ('km', 'ft'): 3280.84,
    ('km', 'yd'): 1093.61,
    ('km', 'mi'): 0.621371,

    ('in', 'mm'): 25.4,
    ('in', 'cm'): 2.54,
    ('in', 'dm'): 0.254,
    ('in', 'm'): 0.0254,
    ('in', 'km'): 0.0000254,
    ('in', 'in'): 1,
    ('in', 'ft'): 0.0833333,
    ('in', 'yd'): 0.0277778,
    ('in', 'mi'): 0.0000157828,

    ('ft', 'mm'): 304.8,
    ('ft', 'cm'): 30.48,
    ('ft', 'dm'): 3.048,
    ('ft', 'm'): 0.3048,
    ('ft', 'km'): 0.0003048,
    ('ft', 'in'): 12,
    ('ft', 'ft'): 1,
    ('ft', 'yd'): 0.333333,
    ('ft', 'mi'): 0.000189394,

    ('yd', 'mm'): 914.4,
    ('yd', 'cm'): 91.44,
    ('yd', 'dm'): 9.144,
    ('yd', 'm'): 0.9144,
    ('yd', 'km'): 0.0009144,
    ('yd', 'in'): 36,
    ('yd', 'ft'): 3,
    ('yd', 'yd'): 1,
    ('yd', 'mi'): 0.000568182,

    ('mi', 'mm'): 1609344,
    ('mi', 'cm'): 160934.4,
    ('mi', 'dm'): 16093.44,
    ('mi', 'm'): 1609.34,
    ('mi', 'km'): 1.60934,
    ('mi', 'in'): 63360,
    ('mi', 'ft'): 5280,
    ('mi', 'yd'): 1760,
    ('mi', 'mi'): 1,
}

def convert_units(input_unit, output_unit, value):
    if (input_unit, output_unit) in conversion_factors:
        return value * conversion_factors[(input_unit, output_unit)]
    else:
        return None

def main():
    input_unit = input("Select any input unit (mm, cm, dm, m, km, in, ft, yd, mi): ")
    output_unit = input("Select desired output unit (mm, cm, dm, m, km, in, ft, yd, mi): ")
    value = float(input("Enter the value to convert: "))

    result = convert_units(input_unit, output_unit, value)
    
    if result is not None:
        print(f"{value} {input_unit} is {result} {output_unit}")
    else:
        print("Conversion not supported.")

    time.sleep(2)

if __name__ == "__main__":
    main()