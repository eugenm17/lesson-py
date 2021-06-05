from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Country", "Capital", "is_russia"]
x.add_row(["Russia", "Moscow", True])
x.add_rows([["Argentina", "Buenos Aires", False], ["Jamaica", "Kingston", False]])
x.add_column("Starts with A", [False, True, False])

print(x)
