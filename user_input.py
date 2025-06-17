to_unit = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * to_unit} {name_of_unit}")
    print(custom_message)


days_to_units(25, "Awsm!")
days_to_units(35, "look good!")
days_to_units(50, "yeah!")
days_to_units(110, "on nooo!")
input()
