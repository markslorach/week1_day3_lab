def return_10():
    return 10

#test 1
def add(number_1, number_2):
    total = number_1 + number_2
    return total

#test2 
def subtract(number_1, number_2):
    total = number_1 - number_2
    return total

#test3
def multiply(number_1, number_2):
    total = number_1 * number_2
    return total

#test4
def divide(number_1, number_2):
    total = number_1 / number_2
    return total

#test5
def length_of_string(string):
    length_int = len(string)
    return length_int

#test6
def join_string(string1, string2):
    joined = string1 + string2
    return joined

#test7
def add_string_as_number(num1, num2):
    total = int(num1) + int(num2)
    return total

#test 8
def number_to_full_month_name(month_int):
    month = {
        1: "January",
        3: "March",
        9: "September"
    }
    month_name = month.get(month_int)
    return month_name
   
