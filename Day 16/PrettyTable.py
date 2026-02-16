from prettytable import PrettyTable

table = PrettyTable()

##Methods are like  functions that can be called
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

##Attributes are like variables that can be changed
table.align = "l"

print(table)