"""Rough satellite pass-window estimator (simplified)."""
import math
from dataclasses import dataclass

EARTH_RADIUS = 6_371_000  # m

@dataclass
class GroundStation:
    lat_deg: float
    lon_deg: float
    min_elevation_deg: float = 5.0

def max_range(orbit_altitude_m: float,
              min_elevation_deg: float) -> float:
    """
    Max slant range from ground station to satellite at minimum elevation.
    Returns range in metres.
    """
    el = math.radians(min_elevation_deg)
    R = EARTH_RADIUS
    h = orbit_altitude_m
    return math.sqrt((R + h)**2 - (R * math.cos(el))**2) - R * math.sin(el)

def contact_arc_deg(orbit_altitude_m: float,
                    min_elevation_deg: float) -> float:
    """Half-angle of the contact arc as seen from Earth's centre."""
    rho = max_range(orbit_altitude_m, min_elevation_deg)
    return math.degrees(math.asin(rho * math.cos(math.radians(min_elevation_deg))
                                  / (EARTH_RADIUS + orbit_altitude_m)))
