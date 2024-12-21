from tokenize import String


def greet(name):
    print("Hello, " + name)
    print(
        "Welcome to 100 Days of Code Python")
    print("This is my first time coding in Python")

greet("Jason")

def life_in_weeks(years):
    x= 4680 - (years* 52)
    print(f"You have {x} weeks left.")
life_in_weeks(20)

def greetPeople(name, city):
    print(f"Hello, {name} from {city}")
greetPeople("Gabriel", "New York")

# TRUE LOVE game calculator



def calculate_love_score(name1, name2):
    count = 0
    total_name = name1 + name2
    for i in total_name:
        if i.lower() == "t":
            count += 1
        elif i.lower() == "r":
            count += 1
        elif i.lower() == "u":
            count += 1
        elif i.lower() == "e":
            count += 1
    count_two = 0
    for i in total_name:
        if i.lower() == "l":
            count_two += 1
        elif i.lower() == "o":
            count_two += 1
        elif i.lower() == "v":
            count_two += 1
        elif i.lower() == "e":
            count_two += 1
    count_str = str(count)
    count_two_str = str(count_two)
    print(count_str + count_two_str)

calculate_love_score("  Kanye West", "Kim Kardashian")


