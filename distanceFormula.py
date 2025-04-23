
def distanceFormula(x1,x2,y1,y2):
    power_x = (x1-x2)**2
    power_y = (y1-y2)**2

    distance = (power_x + power_y)**0.5
    return distance
