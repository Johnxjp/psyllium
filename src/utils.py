def convert_drainage_values(micrometers_per_second: float) -> float:
    """ converts drainage values from micrometers_per_second to inches_per_hour """
    micrometer_per_inch = 25400 
    second_per_hour = 60 * 60
    return micrometers_per_second * (second_per_hour / micrometer_per_inch)

def convert_drainage_values_reverse(inches_per_hour: float) -> float:
    """ converts drainage values from inches_per_hour to micrometers_per_second """
    micrometer_per_inch = 25400 
    second_per_hour = 60 * 60
    return inches_per_hour * (micrometer_per_inch / second_per_hour)