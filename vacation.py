def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte" :
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Not a valid destination"


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7 :
        return cost - 50
    elif days >= 3 :
        return cost - 20
    else :
        return cost

def trip_cost(city, days, spending_money):
    cost_of_trip = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return cost_of_trip

print trip_cost("Los Angeles", 5, 600)
