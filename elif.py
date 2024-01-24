import random
drinks = ["beer", "wine", "whiskey", "rum", "rakija", "campari", "cocktail"]
try:
    age = int(input("How old are you?" ))
    country = input("Where are you from? ")
except ValueError:
    print("I am sorry, but  that is not a valid number")
else:
    # do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")

    if age < 18:
        print("I am sorry, but you are too young to play this drinking game anywhere")
    elif age < 21 and country == "US":
        print("I am sorry, but you are too young to drink in the USA. You can drink elsewhere")
    else:
        drink = random.choice(drinks)
        print("Drink some", drink, "thank you for playing, you are", age, "years old")
