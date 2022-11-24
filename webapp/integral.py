from math import sin


def calc_integral(lower: float, upper: float, parts: int) -> float:
    part_width = (upper - lower) / parts
    # calculating the integral as sum of areas of rectangles.
    # area of each rectangle = part_width * sin(x at the beginning of the part)
    total_area = 0
    for part_num in range(0, parts):
        total_area += part_width * sin(part_num * part_width)
    return (total_area)


def looper(lower: float, upper: float) -> list:
    results = []
    for num_parts in [1, 10, 100, 100, 1000, 10000, 100000, 1000000]:
        results.append(calc_integral(lower, upper, num_parts))
    return results


if __name__ == '__main__':
    print(looper(0, 3.14159))
