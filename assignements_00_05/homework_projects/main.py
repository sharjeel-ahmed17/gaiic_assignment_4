# ==================== 00_intro_python ===========================
# ==================== Question 1 ================================

def calculator ():
    first_number = input("========= enter your first number: =========")
    first_number_to_int = int(first_number)
    second_number = input("========= enter your second number: =========")
    second_number_to_int = int(second_number)

    sum = first_number_to_int + second_number_to_int
    print(sum)

# ==================== Question 2 ================================
def funnny_game():
    user_inp = input("=============   what is your favorite animal : =============\n==================")
    print(f"===========  my favorite animals is also {user_inp}   ===============")

# ==================== Question 3 ================================
def convert_fah_to_cel ():
    degrees_fahrenheit = float(input(f"Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0  
    print(f"Temperature: {degrees_fahrenheit} = {degrees_celsius}")



# ==================== Question 4 ================================
def age_riddle_solve():
    anton = 21
    beth = 6 + anton
    chen= 20 + beth
    drew = chen + anton
    ethan = chen


    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# ==================== Question 5 ================================
def triangle_calculation ():
    len_side_1 = float(input("What is the length of side 1?: "))
    len_side_2 =  float(input("What is the length of side 2?: "))
    len_side_3 = float(input("What is the length of side 3?: "))

    sum_of_triangle = len_side_1 + len_side_2 + len_side_3
    print(f"The perimeter of the triangle: {str(sum_of_triangle)}")

# ==================== Question 6 ================================
def convert_to_squre ():
    square = int(input("enter your number: "))
    final_res = square * square
    print(final_res)
# ==================== Completed ================================


# ==================== 01_expressions ===========================
# ==================== Question 1 ===========================
import random
NUM_SIDES = 6
def roll_dice ():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)
def rolling_dice_3 ():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# ==================== Question 2 ===========================

def mass_calutor ():
    C = 299792458
    mass = float(input("Enter kilos of mass: "))
    e = mass * (C**2)
    print(f"{e}  joules of energy!")
# ==================== Question 3 ===========================


def feet_to_inches ():
    INCHES_IN_FOOT = 12

    feet = int(input("enter feet to convert inches : "))
    res = feet * INCHES_IN_FOOT
    print(res)
# ==================== Question 4 ===========================

def perpendicular_sides():
    import math
    ab = float(input("Enter the length of AB:  "))
    ac = float(input("Enter the length of AC:  "))

    bc = math.sqrt(ab**2 + ac **2)
    print(f"The length of BC (the hypotenuse) is: {bc}")

# ==================== Question 5 ===========================

def remainder ():
    num_1 = int(input("Please enter an integer to be divided: "))
    num_2 = int(input("Please enter an integer to be divided: "))
    res = num_1 % num_2
    print(f"The result of this division is {num_2} with a remainder of {res}")

# ==================== Question 6 ===========================

# aready done with question no 1

# ==================== Question 7 ===========================

def tiny_mad_lib():
    adj = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter.  ")
    verb = input("Please type a verb and press enter. ")
    print(f"Code in Place is fun. I learned to program and used Python to make my {adj} {noun} {verb}!")


def main():
    pass
    # ==== 00_intro_python =====
    # calculator()
    # funnny_game()
    # convert_fah_to_cel()
    # age_riddle_solve()
    # triangle_calculation()
    # convert_to_squre()
    # ==== 01_expression =====
    # rolling_dice_3()
    # mass_calutor()
    # feet_to_inches()
    # perpendicular_sides()
    # remainder()
    # tiny_mad_lib()


if __name__ == "__main__":
    main()

