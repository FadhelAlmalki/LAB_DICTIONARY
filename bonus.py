weather_data = {}

def input_weather_data(weather_data):
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition: ")

    if city not in weather_data:
        weather_data[city] = {}
    
    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print(f"Weather data for {city} on {date} has been added.")

def query_weather_data_by_city(weather_data):
    city = input("Enter city name to query: ")
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, data in weather_data[city].items():
            print(f"Date: {date}, Temperature: {data['temperature']}°C, Humidity: {data['humidity']}%, Condition: {data['condition']}")
    else:
        print(f"No weather data found for {city}.")

def update_weather_data(weather_data):
    city = input("Enter city name to update: ")
    date = input("Enter date (YYYY-MM-DD) to update: ")

    if city in weather_data and date in weather_data[city]:
        temperature = input("Enter new temperature (°C): ")
        humidity = input("Enter new humidity (%): ")
        condition = input("Enter new weather condition: ")

        weather_data[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }

        print(f"Weather data for {city} on {date} has been updated.")
    else:
        print(f"No weather data found for {city} on {date}.")

def delete_weather_data(weather_data):
    city = input("Enter city name to delete: ")
    date = input("Enter date (YYYY-MM-DD) to delete: ")

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        if not weather_data[city]:
            del weather_data[city]
        print("Weather data deleted successfully.\n")
    else:
        print(f"No weather data found for {city} on {date}.")


while True:
    print("Weather Data Management System")
    print("1. Input Weather Data")
    print("2. Query Weather Data")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")

    print("-"*30)

    chosen_option = input("Enter your choice (1-5): ")

    if chosen_option == '1':
        input_weather_data(weather_data)
    elif chosen_option == '2':
        query_weather_data_by_city(weather_data)
    elif chosen_option == '3':
        update_weather_data(weather_data)
    elif chosen_option == '4':
        delete_weather_data(weather_data)
    elif chosen_option == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")