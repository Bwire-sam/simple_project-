def main():
    name = input("Hi. What's your name? ")
    print(user_name(name))
    age = int(input("How old are you? "))
    print(f"\nYou're over {age*365*86400:,} seconds old.\n")
    weight = float(input("Okay, last question. How many pounds do you weigh? "))
    print(f"Moon: {weight*0.166:.2f} lbs | Sun: {weight*27.94:.2f} lbs")

def user_name(name):
    return (f"If poet ee cummings were to email you, he'd address you as {name}\n"
            f"But if ee were mad, he'd call you {name.upper()}")

if __name__ == "__main__":
    main()