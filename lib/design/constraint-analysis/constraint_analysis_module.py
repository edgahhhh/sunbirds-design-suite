# constraint_analysis_module.py
# Author: Edgar Hernandez
# Date: July 19, 2025
# This module contains different functions for conducting a constraint analysis 
# for a conceptual aircraft design.

def TW_desired_tof_distance(mass, wing_area, gravity, density, ground_run, CLmax, CLtof, CDtof, friction_ground):
    """
    Calculate the desired thrust-to-weight ratio for takeoff distance.

    Parameters:
    mass (float): Aircraft mass (kg)
    wing_area (float): Wing area (m^2)
    gravity (float): Acceleration due to gravity (m/s^2)
    density (float): Air density in (kg/m^3)
    tof_distance (float): Takeoff distance in (m)
    cLmax (float): Maximum lift coefficient.
    cLtof (float): Lift coefficient at takeoff.
    cDtof (float): Drag coefficient at takeoff.
    friction_ground (float): Ground friction coefficient.

    Returns:
    float: Thrust-to-weight ratio required for takeoff distance. (N/N)
    """

    # Unpacking parameters
    g = gravity
    rho = density 
    sg = ground_run
    S = wing_area
    mu = friction_ground
    WS_ratio = mass * g / S

    # Calculate the estimated thrust to weight for given weight and wing area
    TW_ratio = 1.21 / (g * rho * CLmax * sg ) * WS_ratio + 0.605 / CLmax * (CDtof + mu * CLtof) * mu

    return TW_ratio