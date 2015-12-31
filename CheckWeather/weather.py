import pywapi

city_ = ""
zip_ = ""
temperature_ = ""
conditions_ = ""
cityID_ = ""


def checkIfValidZip(choice):
    global zip_
    f = open("all_zip_codes.txt", "r")
    found = False
    for line in f.readlines():
        line = line.strip().lower()
        if str(line) == str(choice):
            print("valid")
            found = True
            zip_ = choice
            break
    if found == False:
        choice = input("You did not enter a valid zip code. Please try again: ")
        checkIfValidZip(choice)


def getChoice():
    global city_, zip_
    choice = input("Would you like to find weather for a city(1) or a zip code(2)? ")
    if int(choice) == 1:
        city_ = input("Please enter a city and its state: ")
        return city_
    elif int(choice) == 2:
        zip_ = input("Please enter a zip code: ")
        checkIfValidZip(zip_)
        return zip_
    else:
        print("Your input is not a valid option. Please try again.")
        getChoice()


def getWeather():
    global cityID_, zip_, city_, temperature_, conditions_
    if city_ != "":
        city = pywapi.get_location_ids(city_)
        cityID = list(city.keys())
        tmp = list(city.values())
        city_ = tmp[0]
        cityID_ = cityID
        result = pywapi.get_weather_from_weather_com(cityID[0])
        conditions_ = str(result['current_conditions']['text'])
        temperature_ = float(result['current_conditions']['temperature']) * 1.8 + 32
    else:
        newCity = ""
        zip = pywapi.get_location_ids(zip_)
        cityName = list(zip.values())
        for i in cityName[0]:
            if not i.isdigit() and i != '(' and i != ')':
                newCity += i
        city_ = newCity
        cityList = pywapi.get_location_ids(newCity)
        cityID = list(cityList.keys())
        cityID_ = cityID
        result = pywapi.get_weather_from_weather_com(cityID[0])
        conditions_ = str(result['current_conditions']['text'])
        temperature_ = float(result['current_conditions']['temperature']) * 1.8 + 32


def getWeekOfWeather():
    choice = input("Would you like to see the forecast for the next five days(1) or exit?")
    printWeather(choice)


def printWeather(choice):
    if str(choice) != str(1):
        print("-----------------------------------------------")
        print("City: " + str(city_))
        print("Zip: " + str(zip_))
        print("Temperature: " + str(temperature_) + "°F")
        print("Conditions: " + str(conditions_))
        print("-----------------------------------------------")
        exit(0)
    else:
        result = pywapi.get_weather_from_weather_com(str(cityID_[0]))
        print("----------- Current Conditions ----------------")
        print("City: " + str(city_))
        print("Zip: " + str(zip_))
        print("Temperature: " + str(temperature_) + "°F")
        print("Conditions: " + str(conditions_) + '\n')
        print("----------- 5 Day Forecast --------------------")
        for i in range(0, 5):
            date = str(result['forecasts'][i]['date'])
            dayofweek = str(result['forecasts'][i]['day_of_week'])
            conditions = str(result['forecasts'][i]['day']['brief_text'])
            high = str(float(result['forecasts'][i]['high']) * 1.8 + 32)
            low = str(float(result['forecasts'][i]['low']) * 1.8 + 32)
            print(dayofweek + "," + date + ": High: " + high + "°F Low: " + low + "°F Forecast: " + conditions)
        print("-----------------------------------------------")


if __name__ == '__main__':
    getChoice()
    getWeather()
    getWeekOfWeather()
