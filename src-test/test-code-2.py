


def _is_in_box(
        self,
        aircraft: V2ResponseAcItem,
        lat_south: float,
        lat_north: float,
        lon_west: float,
        lon_east: float,
) -> bool:
    """Check if aircraft is within box bounds.

    Handles longitude wraparound (e.g., box crossing 180° meridian).

    Args:
        aircraft: Aircraft to check
        lat_south: Southern latitude boundary
        lat_north: Northern latitude boundary
        lon_west: Western longitude boundary
        lon_east: Eastern longitude boundary

    Returns:
        True if aircraft is within box bounds, False otherwise
    """
    # Aircraft must have position data
    if aircraft.lat is None or aircraft.lon is None:
        return False

    # Check latitude (straightforward)
    if not (lat_south <= aircraft.lat <= lat_north):
        return False

    # Check longitude (handle wraparound)
    if lon_west <= lon_east:
        # Normal case: box doesn't cross 180° meridian
        return lon_west <= aircraft.lon <= lon_east
    else:
        # Wraparound case: box crosses 180° meridian
        # Aircraft is in box if it's either west of east bound OR east of west bound
        return aircraft.lon >= lon_west or aircraft.lon <= lon_east
