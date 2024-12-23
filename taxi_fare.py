def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    total_fare = base_fare + distance_fare
    return total_fare

def calculate_total_fare(trips):
    total = 0
    fares = []
    for i, distance in enumerate(trips):
        fare = calculate_fare(distance)
        fares.append(f"Trip {i + 1}: ${fare}")
        total += fare
    return fares, total

if __name__ == "__main__":
    trips = [5, 10, 3] 
    fares, total_fare = calculate_total_fare(trips)
    
    for fare in fares:
        print(fare)
    print(f"Total Fare: ${total_fare}")