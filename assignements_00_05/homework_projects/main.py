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
# ==================== 02_lists ===========================
# ==================== Qustion 1 ===========================


def add_tomany_number (numbers):
    total_so_far = 0


    for number in numbers:
        total_so_far += number
    return total_so_far

def add_number ():
    my_number_list = [1, 2, 3, 4, 5]
    sum = add_tomany_number(my_number_list)
    print(f"sum of all numbers : {sum}")
# ==================== Question 2 ===========================
def double_each_element():
    numbers = [1, 2, 3, 4, 5]

    for i in range(len(numbers)):
        elem_at_ind = numbers[i]
        numbers[i] = elem_at_ind * 2 
    
    print(numbers)




# ==================== Question 3 ===========================

# from graphics import Canvas
# skipped
# ==================== Question 4 ===========================

def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def fun_gaming_program():
    # add_three_copies()
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)
# fun_gaming_program()
# ==================== Question 5 ===========================

# def get_first_element(lst):
#     """
#     Prints the first element of a provided list.
#     """

#     print(lst[0])

# # There is no need to edit code beyond this point

# def get_lst():
#     """
#     Prompts the user to enter one element of the list at a time and returns the resulting list.
#     """
#     lst = []
#     elem: str = input("Please enter an element of the list or press enter to stop. ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Please enter an element of the list or press enter to stop. ")
#     return lst

# def get_ele():
#     lst = get_lst()
#     get_first_element(lst)
# get_ele()
# ==================== Question 6 ===========================
def get_last_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[-1])

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def get_ele():
    lst = get_lst()
    get_last_element(lst)
# get_ele()
# ==================== Question 7 ===========================

def get_all_number_list ():
    lst = []  # Make an empty list to store things in

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)
# get_all_number_list()
# ==================== Question 8 ===========================



MAX_LENGTH : int = 3

def shorten(lst):
     while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)
# def main_function ():
def get_list ():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
def main_fun ():
    lst = get_lst()
    shorten(lst)
main_fun()

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
    # done with question no 1
    # tiny_mad_lib()
    # ====== 02_lists =====
    # add_number()
    # double_each_element()

if __name__ == "__main__":
    main()

