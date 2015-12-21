import pywapi
import string

city_ = ""
zip_ = ""


def getChoice():
    global city_, zip_
    choice = input("Would you like to find weather for a city(1) or a zip code(2)? ")
    if int(choice) == 1:
        city_ = input("Please enter a city and its state: ")
        return city_
    elif int(choice) == 2:
        zip_ = input("Please enter a zip code: ")
        return zip_
    else:
        print("Your input is not a valid option. Please try again.")
        getChoice()


def getWeather():
    if city_ != "":
        city = pywapi.get_location_ids(city_)
        cityID = list(city.keys())
        print("city: " + str(city))
        print("val id: " + str(cityID))
        result = pywapi.get_weather_from_weather_com(cityID[0])
        # print("It is " + result["current_conditions"]["text"].lower())
        print("It is " + str(result['current_conditions']['text']) + " and " + result['current_conditions']['temperature'] + "°C now in " + city_ + ".\n\n")
    else:
        newCity = ""
        zip = pywapi.get_location_ids(zip_)
        # print("zip: " + str(zip))
        cityName = list(zip.values())
        # print("r: " + result[0])
        for i in cityName[0]:
            if not i.isdigit() and i != '(' and i != ')':
                newCity += i
        # print("p: " + newCity)
        cityList = pywapi.get_location_ids(newCity)
        # print("t: " + str(cityList))
        cityID = list(cityList.keys())
        result = pywapi.get_weather_from_weather_com(cityID[0])
        print("It is " + str(result['current_conditions']['text']) + " and " + result['current_conditions']['temperature'] + "°C now in " + newCity + ".\n\n")




if __name__ == '__main__':
    getChoice()
    getWeather()