def main():
    year = int(input("Enter your year of birth: "))
    print(age_message(year))

def age_message(year):
    age = 2026 - year
    return f"You are {age} years old you are a young lad"

if __name__ == "__main__":
    main()