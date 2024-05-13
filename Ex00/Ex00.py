#Define the Miles to Km converter function (+ show the difference between the miles and multiply it by kms)
def ConvertMilesToKm(miles):
    return miles * 1.6

#Input the miles/distance that will then be converted to kilometers and then make it appear with the print function.
miles = float(input("Enter distance in miles: "))
kilometers = ConvertMilesToKm(miles)
print(f"{miles} miles is equal to {kilometers} kilometers.")
