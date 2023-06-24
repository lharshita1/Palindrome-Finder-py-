#variable to store a string
check_another = "yes"

#check the variable usong while condition
while check_another == "yes":

#Get the word as an input from user
    my_string = input("Enter your string:- ")

#change the input string to lower case
    my_string = my_string.lower()

#variable for reverse string to store blank string
    rev_string = ""

#take character from input string and combine with reverse string variable
    for char in my_string:
        rev_string = char + rev_string
    
#check both the string are equal or not
    if(my_string == rev_string):
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palinedrome")

#Get the next word as an input from user
    check_another = input("Please enter yes if you want to check another word?")
