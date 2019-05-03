# Python program to sort a list of strings
# lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
lst = [1,5,7,4,89,3]

print("Ascending Order Select 1")
print("Descending Order Select 2")
print("Select your Choice :")
choice = input()

# Display Ascending and Descending Order of Given String
if choice == 1:
    # Using sorted() function
    lst.sort()
    print lst
    # for ele in sorted(lst):
    #     print(ele)

elif choice == 2:
    lst.sort(reverse=True)
    print lst
    # for ele in lst:
    #     print(ele)
else:
    print("Wrong choice entered")