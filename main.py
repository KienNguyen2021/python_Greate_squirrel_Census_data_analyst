import pandas

data = pandas.read_csv("Squirrel_Census.csv")

# take Black from column "Primary Fur Color", then build another csv file

# data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")  -----> create a new csv file

# Now, sort the"grey fur" from Column "Primary Fur Color" :

grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrel)

# Count how many Gray Fur Squirrel:

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel_count)        # 2473


red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(red_squirrel_count)      # 392
print(black_squirrel_count)    #  103

# Create a dictionary for Gray, Cinnamon, Black :

data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count"  : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]

}

print(data_dict)    #   {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [2473, 392, 103]}

# Create a dataFrame :

df = pandas.DataFrame(data_dict)
df.to_csv("squireel_count.csv")    # create a new CSV file
