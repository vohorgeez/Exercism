"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    list_of_wagons = list(args)
    return list_of_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first, second, *rest = each_wagons_id
    new_list = []
    for wagon in rest:
        new_list.append(wagon)
        if wagon == 1:
            new_list.extend(missing_wagons)
    new_list.append(first)
    if first == 1 :
        new_list.extend(missing_wagons)
    new_list.append(second)
    if second == 1 :
        new_list.extend(missing_wagons)
    return new_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops = list(kwargs.values())
    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    exhaustive_route = {**route, **more_route_information}
    return exhaustive_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    order = list(zip(*wagons_rows))
    for i in range(len(order)):
        order[i] = list(order[i])
    return order
