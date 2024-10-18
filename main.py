import time

# Conversion factors for length
length_conversion_factors = {
    ('mcm', 'mm'): 1000,
    ('mcm', 'cm'): 1e-4,
    ('mcm', 'dm'): 1e-5,
    ('mcm', 'm'): 1e-6,
    ('mcm', 'km'): 1e-9,
    ('mcm', 'in'): 3.937e-5,
    ('mcm', 'ft'): 3.2808e-6,
    ('mcm', 'yd'): 1.0936e-6,
    ('mcm', 'mi'): 6.21363636364e-10,

    ('mm', 'mcm'): 1000,
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

# Conversion factors for volume
volume_conversion_factors = {
    ('L', 'mL'): 1000,
    ('L', 'cm³'): 1000,
    ('L', 'm³'): 0.001,
    ('L', 'gal'): 0.264172,
    ('L', 'qt'): 1.05669,
    ('L', 'pt'): 2.11338,
    ('L', 'fl oz'): 33.814,
    
    ('mL', 'L'): 0.001,
    ('mL', 'cm³'): 1,
    ('mL', 'm³'): 1e-6,
    ('mL', 'gal'): 0.000264172,
    ('mL', 'qt'): 0.00105669,
    ('mL', 'pt'): 0.00211338,
    ('mL', 'fl oz'): 0.033814,
    
    ('cm³', 'L'): 0.001,
    ('cm³', 'mL'): 1,
    ('cm³', 'm³'): 1e-6,
    ('cm³', 'gal'): 0.000264172,
    ('cm³', 'qt'): 0.00105669,
    ('cm³', 'pt'): 0.00211338,
    ('cm³', 'fl oz'): 0.033814,

    ('m³', 'L'): 1000,
    ('m³', 'mL'): 1e6,
    ('m³', 'cm³'): 1e6,
    ('m³', 'gal'): 264.172,
    ('m³', 'qt'): 1056.69,
    ('m³', 'pt'): 2113.38,
    ('m³', 'fl oz'): 33814,

    ('gal', 'L'): 3.78541,
    ('gal', 'mL'): 3785.41,
    ('gal', 'cm³'): 3785.41,
    ('gal', 'm³'): 0.00378541,
    ('gal', 'qt'): 4,
    ('gal', 'pt'): 8,
    ('gal', 'fl oz'): 128,

    ('qt', 'L'): 0.946353,
    ('qt', 'mL'): 946.353,
    ('qt', 'cm³'): 946.353,
    ('qt', 'm³'): 0.000946353,
    ('qt', 'gal'): 0.25,
    ('qt', 'pt'): 2,
    ('qt', 'fl oz'): 32,

    ('pt', 'L'): 0.473176,
    ('pt', 'mL'): 473.176,
    ('pt', 'cm³'): 473.176,
    ('pt', 'm³'): 0.000473176,
    ('pt', 'gal'): 0.125,
    ('pt', 'qt'): 0.5,
    ('pt', 'fl oz'): 16,

    ('fl oz', 'L'): 0.0295735,
    ('fl oz', 'mL'): 29.5735,
    ('fl oz', 'cm³'): 29.5735,
    ('fl oz', 'm³'): 2.95735e-5,
    ('fl oz', 'gal'): 0.0078125,
    ('fl oz', 'qt'): 0.03125,
    ('fl oz', 'pt'): 0.0625,
}

def convert_length_units(input_unit, output_unit, value):
    if (input_unit, output_unit) in length_conversion_factors:
        return value * length_conversion_factors[(input_unit, output_unit)]
    else:
        return None

def convert_volume_units(input_unit, output_unit, value):
    if (input_unit, output_unit) in volume_conversion_factors:
        return value * volume_conversion_factors[(input_unit, output_unit)]
    else:
        return None

def main():
    conversion_type = input("Select conversion type (length/volume): ").strip().lower()

    if conversion_type == 'length':
        input_unit = input("Select input unit (mcm, mm, cm, dm, m, km, in, ft, yd, mi): ")
        output_unit = input("Select desired output unit (mcm, mm, cm, dm, m, km, in, ft, yd, mi): ")
        value = float(input("Enter the value to convert: "))
        
        result = convert_length_units(input_unit, output_unit, value)
        
        if result is not None:
            print(f"{value} {input_unit} is {result} {output_unit}")
        else:
            print("Conversion not supported.")

    elif conversion_type == 'volume':
        input_unit = input("Select input unit (L, mL, cm³, m³, gal, qt, pt, fl oz): ")
        output_unit = input("Select desired output unit (L, mL, cm³, m³, gal, qt, pt, fl oz): ")
        value = float(input("Enter the value to convert: "))
        
        result = convert_volume_units(input_unit, output_unit, value)
        
        if result is not None:
            print(f"{value} {input_unit} is {result} {output_unit}")
        else:
            print("Conversion not supported.")
    
    else:
        print("Invalid conversion type selected.")

    time.sleep(2)

if __name__ == "__main__":
    main()