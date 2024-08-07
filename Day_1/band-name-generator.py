print("Welcome to the Band Name Generator.")

cityName = input("Wha's name of the city you grew up in ? \n")

petName = input("What's your pet's name? \n")

bandName = cityName[0:3] + petName[0:2]

print("Your band name could be " + bandName)