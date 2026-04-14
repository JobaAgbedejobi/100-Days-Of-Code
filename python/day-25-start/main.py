import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colour = data["Primary Fur Color"]
#print(colour)
colour_list = colour.to_list()
#print(colour_list)
Grey = colour_list.count("Gray")
Cinnamon = colour_list.count("Cinnamon")
Black = colour_list.count("Black")
data_dict = {
    "Colour" : ["Gray", "Cinnamon", "Black"],
    "Count" : [Grey, Cinnamon, Black]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")