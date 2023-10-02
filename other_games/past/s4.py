# for i in range(5):
#     print("hello")
#     print("")
# print()

# i = 0
# while i < 5:
#     print("hello")
#     i += 1  # i = i + 1

# quit = "no"
# while quit == "no":
#     quit = input("Do you want to quit?(yes or no?) ")

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit == "yes":
#         done = True
#     attack = input("Does your elf attack the dragon? ")
#     if attack == "yes":
#         print("Bad choice, you died.")
#         done = True


import random
# x = random.randrange(10)
# print(x)
# for i in range(100):
#     x = random.randrange(1, 11)
#     print(x)

numbers = [1, 2, 3, 4, 5]
# print(len(numbers))
# random_index = random.randrange(len(numbers))
# print(numbers[random_index])

CHOICES = ("r", "p", "s")
# random_index = random.randrange(len(CHOICES))
# print(random_index)
# print(CHOICES[random_index])
# print(random.choice(CHOICES))
computer_hand = random.choice(CHOICES)
user_hand = input('enter your choice("r", "p", "s") ')

print("user choice: ", user_hand)
print("user computer: ", computer_hand)

if user_hand == "r":
    if computer_hand == "p":
        print("computer is winner.")
    elif computer_hand == "s":
        print("user is winner")
    elif computer_hand == "r":
        print("both equal")
elif user_hand == "p":
    pass
    
