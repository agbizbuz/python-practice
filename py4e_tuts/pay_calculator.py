def paycalc_conditional():
    """
    conditional pay calculator
    """
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Hourly rate:")
    rt = float(rate)
    pay = 0.0
    if h > 40:
        extra = h - 40
        pay = 40 * rt + extra * rt * 1.5
    else:
        pay = h * rt
        
    print(pay)

def computepay(hrs, rate):
    """
    calculates payment given hours and hourly rate
    """
    pay = 0.0
    hrs = float(hrs)
    rate = float(rate)
    if hrs > 40:
        extra = hrs - 40
        pay = 40 * rate + extra * rate * 1.5
    else:
        pay = hrs * rate
        
    return pay