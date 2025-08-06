# capital.py

def capital(capitals,):
    result = []
    for place in capitals:
        location_key = 'state' if 'state' in place else 'country'
        location_name = place[location_key]
        capital_name = place['capital']
        result.append(f"The capital of {location_name} is {capital_name}")
    return result

capitals_list = [
    {'state': 'Kenya', 'capital': 'Nairobi'}
]

print(capital(capitals_list))
