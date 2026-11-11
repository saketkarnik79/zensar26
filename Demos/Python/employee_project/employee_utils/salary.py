def calculate_gross_salary(basic, hra, bonus):
    return basic + hra + bonus

def calculate_net_salary(gross, tax):
    return gross - tax