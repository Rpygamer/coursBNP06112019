def is_car(list_car, position):
    """
        return True if there is a car 
        on this position
    """
    for car in list_car:
        if car["position"] == position:
            return True
    return False
            
def display_board(list_car):
    """
        Display a map (10x10) on console output
        A car is represented by "x"
        no car is represented by " "
        :param list_car: List of car position
        
        :Example:
        >>> display_board([{
                'marque': 'Mercedes',
                'position': (3, 1),
                'direction': (0, 1)
            }])
    """
    for i in range(10):
        line = []
        for j in range(10):
            if is_car(list_car, (i,j)):
                line.append("x")
            else:
                line.append(".")
        print("".join(line))

print(__name__)
if __name__ == "__main__":
    display_board([(3,2), (6,1)])