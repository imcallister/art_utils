from calysto.graphics import Color


def hump(x):
    x = x % 360
    if x > 240:
        return 0
    elif x >= 0 and x <= 60:
        return float(x) / 60.0
    elif x > 60 and x <= 180:
        return 1.0
    else:
        return float(240 - x) /60.0
    
def red(x):
    return int(254 * hump(x-240))

def green(x):
    return int(254 * hump(x))

def blue(x):
    return int(254 * hump(x-120))


def color_wheel(x):
    return Color(red(x), green(x), blue(x))
