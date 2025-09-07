"""Module for working with 3D coordinates."""

def generate_combinations(max_x: int, max_y: int, max_z: int) -> list[dict]:
    """
    Generates all possible coordinate combinations from (0,0,0) to (max_x, max_y, max_z)
    by sequentially moving along the x, y, z axes.
    """
    def _generate_axis(axis: str, max_value: int, current_coords: list[dict]) -> None:
        """Generates coordinates along a single axis."""
        new_coords = []
        for coord in current_coords:
            for step in range(1, max_value + 1):
                new_coord = coord.copy()
                new_coord[axis] += step
                new_coords.append(new_coord)
        current_coords.extend(new_coords)

    coords_combination = []
    initial_coord = {"x": 0, "y": 0, "z": 0}
    coords_combination.append(initial_coord)

    _generate_axis("x", max_x, coords_combination)
    _generate_axis("y", max_y, coords_combination)
    _generate_axis("z", max_z, coords_combination)

    coords_combination.sort()

    return coords_combination


def filter_by_sum(coordinates: list[dict], target_sum: int) -> list[dict]:
    """Filters coordinates, removing those where the sum of axis values equals target_sum."""
    return [
        coord for coord in coordinates 
        if coord["x"] + coord["y"] + coord["z"] != target_sum
    ]


def print_coords(coordinates: list[dict]) -> None:
    """Prints a list of coordinates in the format: x: value, y: value, z: value"""
    for coordinate in coordinates:
        print(f"x: {coordinate['x']}, y: {coordinate['y']}, z: {coordinate['z']}")