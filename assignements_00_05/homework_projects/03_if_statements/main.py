# ==================== Question 1 ===========================
def print_events():
    # for i in range(0, 21, 2):
    #     print(i)
    for i in range(20):
        print(i * 2)

# ==================== Question 2 ===========================

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def internation_voting_age():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# There is no need to edit code beyond this point



# ==================== Question 3 ===========================
def leap_year():
    year = int(input("please enter a year: "))

    if year % 4 == 0: 
        if year % 100 == 0:
            if year % 400 == 0:
                print("this is a leap year")
            else : 
                print("this is not a leap year")
        else: 
            print("that is a leap year")
    else : 
        print("that's is not a leap year")
# ==================== Question 4 ===========================
def tall_to_ride ():
    MINIMUM_HEIGHT= 50

    height = float(input("enter your height: "))
    while height >= MINIMUM_HEIGHT:
        print("you are tall enogh to ride")
    else : 
        print("you are not are tall enogh to ride")
    # while height < MINIMUM_HEIGHT:
    #     print("")
# ==================== Question 5 ===========================

import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def random_number_generator():
    rnd = random.randrange(MIN_VALUE , MAX_VALUE , N_NUMBERS)
    print(rnd)

def main():
    pass
    # print("hello world")
    # print_events()
    # internation_voting_age()
    # leap_year()
    # tall_to_ride()
    random_number_generator()
if __name__ == "__main__":
    main()