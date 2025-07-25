# TAKEOFF_MODULE.py
# Author: Edgar Hernandez
# Date: July 19, 2025
# This module contains functions relevant to the performance of an aircraft during takeoff.
# The main purpose is to provide functions to develop CL and CD at some conditions while correcting for ground effect.

# Equations are provided from S. Gudmundsson's "Introduction to Aircraft Design" 

def lift_correction_factor(CL, wingspan, aspect_ratio, taper_ratio, wing_efficiency, height_agl):
    """
    This function calculates the lift correction factor for ground effect.
    The relationship is for the case of a tapered wing, where the taper ratio and the aspect ratio drive the correction.
    Other values, such as the wing efficiency factor, are also considered.

    Theory Overview:
    CLge  = phiL * CL
    where phiL is the lift correction factor for ground effect.

    """

    # unpacking inputs
    b = wingspan
    AR = aspect_ratio
    TR = taper_ratio
    e = wing_efficiency
    h = height_agl
    hb_ratio = h/b


    deltaL = 1.225*(TR**(0.00273) - 0.997) * (AR**(0.717) + 13.6)
    betaL = 1 + (0.269*CL**(1.45))/(AR**(3.18) * hb_ratio**(1.12))
    
    # Calculating the ground effect correction factor for lift, AKA phiL
    phiL = 1/betaL *(1+deltaL * (288*hb_ratio**(0.787)) / (AR**(0.882)) * e **(-9.14*hb_ratio**(0.327)))
    
    ground_effect_factor_CL = phiL

    return ground_effect_factor_CL

def drag_correction_factor(CL, wingspan, aspect_ratio, taper_ratio, wing_efficiency, height_agl):
    """
    This function calculates the drag correction factor for ground effect.
    The relationship is for the case of a tapered wing. 

    Theory Overview:
    CDge = phiL^2 - phiD * CD 
    where phiL is the lift correction factor and phiD is the drag correction factor.

    """

        # unpacking inputs
    b = wingspan
    AR = aspect_ratio
    TR = taper_ratio
    e = wing_efficiency
    h = height_agl
    hb_ratio = h/b

    deltaD = 1-0.157 * (TR**(0.775) - 0.378) * (AR**(0.417) - 1.27)
    betaD = 1 + (0.0361 * CL**(1.21)) / (AR**(1.19) * hb_ratio**(1.51))

    phiD = betaD * (1 - deltaD * e **(-4.74 * hb_ratio **(0.814))) - hb_ratio **2 * e**(-3.88 * hb_ratio**(0.758))

    ground_effect_factor_CD = phiD

    return ground_effect_factor_CD

def ground_effect_factors(CL, wingspan, aspect_ratio, taper_ratio, wing_efficiency, height_agl):


    phiL = lift_correction_factor(CL, wingspan, aspect_ratio, taper_ratio, wing_efficiency, height_agl)
    phiD = drag_correction_factor(CL, wingspan, aspect_ratio, taper_ratio, wing_efficiency, height_agl)

    ground_effect_factor_CL = phiL
    ground_effect_factor_CD = phiD

    return ground_effect_factor_CL, ground_effect_factor_CD