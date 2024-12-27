from random import randint
dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

try:
    age = int(input("What is your age?: "))
except ValueError:
    print("You have typed in an invalid number. Please put an integer such as 15.")
    age = int(input("What is your age? "))

if age > 18:
    print(f"You can drive at age {age}.")


