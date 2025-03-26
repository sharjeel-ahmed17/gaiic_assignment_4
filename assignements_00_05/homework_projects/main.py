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
# ==================== Question 3 ================================
# ==================== Question 3 ================================

def main():
    pass
    # calculator()
    # funnny_game()
    # convert_fah_to_cel()
    # age_riddle_solve()
    # triangle_calculation()
    # convert_to_squre()


if __name__ == "__main__":
    main()

