Weather = str(input(f"What is the waeather like today? (sunny, rainy or cold):  " ))
if Weather == "sunny":
    print(f"Wear a T-shirt and sunglasses.")
elif Weather == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif Weather == "cold":
    print(f"Make sure to wear a warm cloth and a scarf.")
else:
    print("Sorry, I don't have a recommendations for this weather.")