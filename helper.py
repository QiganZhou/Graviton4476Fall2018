# This module contains low-level helper functions.

import numpy as np

# Convert a numerical angle in radian to string.
# For example, np.pi will be converted to "180.00dg"
# by default.
def angToStr(ang, toDeg=True, dec=2, showPi=True):
    pi = np.pi
    if toDeg:
        return "{:.{prec}f}dg".format(ang*180/pi, prec=dec)
    elif showPi:
        return "{:.{prec}f}pi".format(ang/pi, prec=dec)
    else:
        return "{:.{prec}f}rad".format(ang, prec=dec)

