from Order.models import Order
from Meniu.models import Menu

def validateString(string):
    try:
        y = int(string)
        return False
    except:
        return True

def validateCode(string):
    if validateString(string) == False:
        return False
    cod = string.split("-")
    if len(cod) != 2:
        return False
    try:
        int(cod[0])
        int(cod[1])
    except:
        return False
    codMeniu = cod[0]
    codOrder = cod[1]
    try:
        meniu = Menu.objects.get(pk=codMeniu)
        comanda = Order.objects.get(pk=codOrder)
    except:
        return False
    tup = (codMeniu,codOrder)
    return tup