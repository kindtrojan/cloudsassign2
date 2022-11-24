import logging

import azure.functions as func


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
    for num_parts in [1, 10, 100, 100, 1000, 10000, 100000]:
        results.append(calc_integral(lower, upper, num_parts))
    return results


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        lower = req.route_params.get('lower')
        upper = req.route_params.get('upper')
    except:
         return func.HttpResponse(
             "This HTTP request is not properly formed with all required inputs",
             status_code=200
    )   

    result = looper(float(lower), float(upper))
    return func.HttpResponse(
             f'Integral result: {result}',
             status_code=200
    )
