def move_cars(list_car):
    """
        return new list of positions
        each car moves one step to the top
        (+1 on y-axis)
        :param list_car: List of cars to move
        :return: list of new positions
        
        :Example:
        >>> move_cars([(1,2), (5,3)])
        [(1,3), (5,4)]
    """
    for car in list_car:
        new_position = car["position"] + car["direction"]
        if (new_position < 0).any() or (new_position >= 10).any():
            turn_car(car)
        else:
            car["position"] = new_position
    return list_car
    
