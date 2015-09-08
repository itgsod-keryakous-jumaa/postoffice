
def is_envelop(width,length,thickness):
    """

    :param width:
    :param length:
    :param thickness:
    :return: True or False
    """

    #code ....

    return True


# START

def weight(vikt):
    if vikt > 2 or vikt <= 0:
        return False
    else:
        return True

def meassurements(lenght, width, thickness):
    if lenght >= 14 and lenght <= 60 and width >= 9 and lenght + width + thickness <= 90 and lenght + width + thickness > 0:
        return True
    else:
        return False



def  fetch_values(vikt,lenght, width, thickness):
    grillkorv = weight(vikt)
    ketchup = meassurements(lenght, width, thickness)
    if grillkorv == True and ketchup == True:
        return True
    else:
        return False


