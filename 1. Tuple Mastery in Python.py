# 1. Tuple Mastery in Python

def flight_itinerary(flight_list):
    for idx, passenger in enumerate(flight_list, 1):
        name, from_city, to_city = passenger
        print(f"Itinerary {idx}: {name} - from {from_city} to {to_city}")

flight_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
flight_itinerary(flight_list)