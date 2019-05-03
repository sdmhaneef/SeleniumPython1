#Question : Write a program to check if prefix and suffix of a string is a palindrome
# Function to check whether
# the string is a palindrome
def is_palindrome(r):
    # Reverse the string and assign
    # it to new variable for comparison
    p = r[::-1]
    if(r == p ):
        # print(r)
        # print True
        return True
    else:
        return False


# Function to check whether the string
# has prefix and suffix substrings
def check_str(stext):
    l = len(stext)
    # check all prefix substrings
    temp = 2
    for temp in range(2,l+1):
        # check if the prefix substring
        # is a palindrome
        if is_palindrome(stext[0:temp]) == True:
            return True
            break
        else:
            temp = temp+1


# Driver code
if __name__ == '__main__':
    print("Program to check if prefix and suffix of a string is a palindrome")
    print("Enter a string :")
    val = raw_input()
    revText = val[::-1]
    if check_str(val) == True and check_str(revText) == True:
        print("YES")
    else:
        print("NO")

