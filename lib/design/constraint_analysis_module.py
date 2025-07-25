# constraint_analysis_module.py
# Author: Edgar Hernandez
# Date: July 19, 2025
# This module contains different functions for conducting a constraint analysis 
# for a conceptual aircraft design.

def TW_desired_tof(density, ground_run, CLmax, CLtof, CDtof, friction_ground, mass=None, gravity=None,
    wing_area=None, wing_loading=None, use_wing_loading=False):
    """
    Calculate the desired thrust-to-weight ratio for takeoff distance.

    Parameters:
    - density (float): Air density (kg/m^3)
    - ground_run (float): Takeoff ground run distance (m)
    - CLmax (float): Maximum lift coefficient
    - CLtof (float): Lift coefficient at takeoff
    - CDtof (float): Drag coefficient at takeoff
    - friction_ground (float): Ground friction coefficient
    - mass (float, optional): Aircraft mass (kg)
    - gravity (float, optional): Gravity acceleration (m/s^2)
    - wing_area (float, optional): Wing area (m^2)
    - wing_loading (float, optional): Wing loading (N/m^2)
    - use_wing_loading (bool, optional): If True, use wing_loading directly

    Returns:
    - float: Thrust-to-weight ratio required for takeoff distance (dimensionless)
    """

    g = gravity if gravity is not None else 9.81  # default gravity if not given

    if use_wing_loading:
        if wing_loading is None:
            raise ValueError("wing_loading must be provided if use_wing_loading=True")
        WS_ratio = wing_loading
    else:
        if None in (mass, gravity, wing_area):
            raise ValueError("mass, gravity, and wing_area must be provided if use_wing_loading=False")
        WS_ratio = mass * g / wing_area

    TW_ratio = 1.21 / (g * density * CLmax * ground_run) * WS_ratio + 0.605 / CLmax * (CDtof + friction_ground * CLtof) * friction_ground

    return TW_ratio

# OLD VERSION
# def TW_desired_tof_distance(mass, wing_area, gravity, density, ground_run, CLmax, CLtof, CDtof, friction_ground):
#     """
#     Calculate the desired thrust-to-weight ratio for takeoff distance.

#     Parameters:
#     mass (float): Aircraft mass (kg)
#     wing_area (float): Wing area (m^2)
#     gravity (float): Acceleration due to gravity (m/s^2)
#     density (float): Air density in (kg/m^3)
#     tof_distance (float): Takeoff distance in (m)
#     cLmax (float): Maximum lift coefficient.
#     cLtof (float): Lift coefficient at takeoff.
#     cDtof (float): Drag coefficient at takeoff.
#     friction_ground (float): Ground friction coefficient.

#     Returns:
#     float: Thrust-to-weight ratio required for takeoff distance. (N/N)
#     """

#     # Unpacking parameters
#     g = gravity
#     rho = density 
#     sg = ground_run
#     S = wing_area
#     mu = friction_ground
#     WS_ratio = mass * g / S

#     # Calculate the estimated thrust to weight for given weight and wing area
#     TW_ratio = 1.21 / (g * rho * CLmax * sg ) * WS_ratio + 0.605 / CLmax * (CDtof + mu * CLtof) * mu

#     return TW_ratio