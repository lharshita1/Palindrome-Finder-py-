# get the word as an input from user
my_string = input("Enter a String - ")

#change the input string to lower case
my_string_lower = my_string.lower()

# find the length of the string
len_string = len(my_string_lower)

#set indexes to check extract each letter of the string
i=0
j=len_string-1

#check is the ltters in the word are same or not when the word is reversed
for i in range(len_string):

#set the flag to 1st if the 1st and the last index is same
    if(my_string_lower[i] == my_string_lower[j]):

        i=i+1
        j=j-1
        flag =1
    else:
        flag = 0 
        break

if(flag == 1):
    print("it's a Palindrome")
if(flag == 0):
    print("it's Not a Palindrome")
        
