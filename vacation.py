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

def your_trip():
    city = raw_input("Which city are you going to?")
    days = raw_input("How many days are you going for?")
    spending_money = raw_input("How much are you spending?")

    print "So You are going to %s for %d days and have %d spending money?" % (city, days, spending_money)
    return trip_cost(city, days, spending_money)


your_trip()
