class DestinationOption:
    def __init__(self, name, activities, accessibility, weather, cost):
        self.name = name
        self.activities = activities
        self.accessibility = accessibility
        self.weather = weather
        self.cost = cost

option_A = DestinationOption(
    name="Seaside Resort",
    activities=["diving", "snorkeling"],
    accessibility="Easy access by car or plane",
    weather="Warm and sunny",
    cost=1500
)

option_B = DestinationOption(
    name="Mountain Excursion",
    activities=["hiking", "landscape exploration"],
    accessibility="More challenging access, requires suitable transport",
    weather="Cool and sunny",
    cost=1200
)

option_C = DestinationOption(
    name="Historical City Trip",
    activities=["museum visits", "monument exploration"],
    accessibility="Easy access by public transport",
    weather="Moderate and variable",
    cost=1000 
)

def evaluate_destinations(budget, personal_interests, preferred_weather):
    options = [option_A, option_B, option_C]
    valid_options = []

    for option in options:
        if option.cost <= budget:
            valid_options.append(option)

    filtered_options = []
    for option in valid_options:
        if any(activity.strip().lower() in [act.strip().lower() for act in option.activities] for activity in personal_interests):
            if option.weather.strip().lower() == preferred_weather.strip().lower():
                filtered_options.append(option)

   
    if filtered_options:
        best_option = min(filtered_options, key=lambda x: len(x.accessibility))
        return best_option
    else:
        return None

budget = float(input("Enter your available budget (in EUR): "))
personal_interests = input("Enter your preferred activities (e.g., diving, snorkeling, hiking): ").split(",")
preferred_weather = input("Enter your preferred weather conditions (e.g., Warm and sunny, Cool and sunny): ")

best_destination = evaluate_destinations(budget, personal_interests, preferred_weather)


if best_destination:
    print(f"The best destination for you is: {best_destination.name}")
else:
    print("There is no suitable destination under these conditions.")
