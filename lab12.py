import json
from datetime import datetime

# Початкові дані поїздів
trains = [
    {"number": "101", "route": "Kyiv - Kharkiv", "arrival": "12:30", "departure": "12:50"},
    {"number": "102", "route": "Lviv - Odesa", "arrival": "14:00", "departure": "14:20"},
    {"number": "103", "route": "Dnipro - Zaporizhzhia", "arrival": "09:15", "departure": "09:45"},
    {"number": "104", "route": "Kyiv - Lviv", "arrival": "11:00", "departure": "11:30"},
    {"number": "105", "route": "Kharkiv - Odesa", "arrival": "15:45", "departure": "16:05"},
    {"number": "106", "route": "Odesa - Kyiv", "arrival": "17:10", "departure": "17:30"},
    {"number": "107", "route": "Lviv - Kyiv", "arrival": "18:20", "departure": "18:40"},
    {"number": "108", "route": "Kyiv - Dnipro", "arrival": "13:15", "departure": "13:35"},
    {"number": "109", "route": "Odesa - Lviv", "arrival": "10:00", "departure": "10:20"},
    {"number": "110", "route": "Sumy - Kyiv", "arrival": "16:45", "departure": "17:05"}
]

# Збереження даних у JSON-файл з відступами для форматування
with open("trains_data.json", "wt") as file:
    json.dump(trains, file, indent=4)

# Функція для перевірки правильності формату часу
def validate_time(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%H:%M')
        if time_obj.hour > 23 or time_obj.minute > 59:
            raise ValueError
        return True
    except ValueError:
        return False

# Основне меню програми
while True:
    print("Select an option:\n 1 - Add a train\n 2 - View all trains by arrival time\n 3 - Find train by route or number\n 4 - Exit")
    option = int(input("Choose an option: "))

    # Додавання нового поїзда
    if option == 1:
        with open("trains_data.json", "rt") as file:
            trains = json.load(file)

        def add_train(trains):
            print("Add a new train:")
            number = input("Train number: ")
            route = input("Route (e.g., Kyiv - Kharkiv): ")

            # Введення часу прибуття з перевіркою
            while True:
                arrival = input("Arrival time (HH:MM): ")
                if validate_time(arrival):
                    break
                else:
                    print("Invalid time format or value! Please enter a valid time (HH:MM) with hours ≤ 23 and minutes ≤ 59.")

            # Введення часу відправлення з перевіркою
            while True:
                departure = input("Departure time (HH:MM): ")
                if validate_time(departure):
                    break
                else:
                    print("Invalid time format or value! Please enter a valid time (HH:MM) with hours ≤ 23 and minutes ≤ 59.")

            trains.append({"number": number, "route": route, "arrival": arrival, "departure": departure})
            return trains

        trains = add_train(trains)

        with open("trains_data.json", "wt") as file:
            json.dump(trains, file, indent=4)

        print("Train added successfully.")

    # Відображення всіх поїздів за часом прибуття
    elif option == 2:
        with open("trains_data.json", "rt") as file:
            trains = json.load(file)

            # Сортування поїздів за часом прибуття
            sorted_trains = sorted(trains, key=lambda train: datetime.strptime(train['arrival'], '%H:%M'))

            print("Trains sorted by arrival time:")
            for train in sorted_trains:
                print(f"Train {train['number']}, Route: {train['route']}, Arrival: {train['arrival']}, Departure: {train['departure']}")

    # Пошук поїзда за номером або маршрутом
    elif option == 3:
        with open("trains_data.json", "rt") as file:
            trains = json.load(file)

        search_type = input("Search by 'number' or 'route': ").strip().lower()
        search_value = input(f"Enter {search_type}: ")

        found_trains = [train for train in trains if train[search_type] == search_value]

        if found_trains:
            for train in found_trains:
                print(train)
        else:
            print(f"No trains found for {search_type} = {search_value}")

    # Вихід з програми
    elif option == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid option, please try again.")
