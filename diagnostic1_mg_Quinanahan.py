def calculate_space_weight(earth_weight, destination):
    if destination == "mars":
        new_weight = earth_weight*0.38
    elif destination == "jupiter":
       new_weight = earth_weight*2.34
    elif destination == "moon":
        new_weight = earth_weight*0.16
    else:   
        print("Invalid destination, Please input either, Mars, Jupiter, or the moon")
        return None
    return new_weight


def main():

    print("Please input your weight on earth and your destination")
    earthweight = float(input("earthweight:"))
    destination = input("destination:")
    new_weight = calculate_space_weight(earthweight,destination)
    print(f"Your weight on {destination}: is {new_weight}")


main()