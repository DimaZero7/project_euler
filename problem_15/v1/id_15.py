# https://projecteuler.net/problem=15
# python 3.11
from utils import performance_decorator


def calculate_options_for_rectangle(length: int, height: int, cache_cubes: dict) -> None:
    if length == 1:
        cache_cubes[str(length) + ';' + str(height)] = 2 + height - 1
        cache_cubes[str(height) + ';' + str(length)] = 2 + height - 1
    else:
        number_options = 2

        length_entry_points = length - 1
        height_entry_points = height - 1

        for length_entry_point in range(1, length_entry_points + 1):
            length_small_cube = length - length_entry_point
            height_small_cube = height - 1

            key = str(length_small_cube) + ';' + str(height_small_cube)
            if key in cache_cubes:
                number_options += cache_cubes[key]

        for height_entry_point in range(1, height_entry_points + 1):
            length_small_cube = length - 1
            height_small_cube = height - height_entry_point

            key = str(length_small_cube) + ';' + str(height_small_cube)
            if key in cache_cubes:
                number_options += cache_cubes[key]

        cache_cubes[str(length) + ';' + str(height)] = number_options
        cache_cubes[str(height) + ';' + str(length)] = number_options


@performance_decorator
def main():
    # stores size_side_cube: number_options
    cache_cubes = {'1;1': 2}

    for cube_side_size in range(2, 21):
        number_options = 2

        length = cube_side_size
        height = cube_side_size

        entry_points = cube_side_size - 1

        for entry_point in range(1, entry_points + 1):
            length_small_cube = length - entry_point
            height_small_cube = height - 1

            key = str(length_small_cube) + ';' + str(height_small_cube)
            if key in cache_cubes:
                number_options += cache_cubes[key] * 2
            else:
                calculate_options_for_rectangle(
                    length=length_small_cube,
                    height=height_small_cube,
                    cache_cubes=cache_cubes
                )
                number_options += cache_cubes[key] * 2

        cache_cubes[str(length) + ';' + str(height)] = number_options
        cache_cubes[str(height) + ';' + str(length)] = number_options

    print(cache_cubes)


main()
