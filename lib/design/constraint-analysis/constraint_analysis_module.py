# constraint_analysis_module.py
# Author: Edgar Hernandez
# Date: July 19, 2025
# This module contains different functions for conducting a constraint analysis 
# for a conceptual aircraft design.

def TW_desired_tof_distance(weight, wing_area, gravity, density, tof_distance, cLmax, cLtof, cDtof, friction_ground):
    """
    Calculate the desired thrust-to-weight ratio for takeoff distance.

    Parameters:
    weight (float): Aircraft weight in Newtons.
    wing_area (float): Wing area in square meters.
    gravity (float): Acceleration due to gravity in m/s^2.
    density (float): Air density in kg/m^3.
    tof_distance (float): Takeoff distance in meters.
    cLmax (float): Maximum lift coefficient.
    cLtof (float): Lift coefficient at takeoff.
    cDtof (float): Drag coefficient at takeoff.
    friction_ground (float): Ground friction coefficient.

    Returns:
    float: Thrust-to-weight ratio required for takeoff distance.

    Description:
    This function assumes that the aircraft is lifting off 10% faster than the stalling speed.
    Where the stalling speed is estimated from the cL equation.
    """

    # Calculate the required lift force
    lift_force = weight * gravity
    
    # Calculate the required thrust force
    thrust_force = lift_force / cLtof * cLmax / cDtof
    
    # Calculate the desired thrust-to-weight ratio
    TW_ratio = thrust_force / weight
    
    return TW_ratio