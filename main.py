#Task 1
#Approach 1
cat_age = int(input("Age: "))
if cat_age <= 6:
    print("Price is $250 for a kitten. ")
elif cat_age <= 11:
    print("Price is $225 for a teenager.")
elif cat_age <= 95:
    print("Price is $150 for an adult.")
elif cat_age >= 96:
    print("Price is $85 for a senior.")

#Approach 2
cat_age = int(input("Age: "))
if cat_age >= 96:
    print("Price is $85 for a senior.")
elif cat_age <= 95:
    print("Price is $150 for an adult.")
elif cat_age <= 11:
    print("Price is $225 for a teenager.")
elif cat_age <= 6:
    print("Price is $250 for a kitten.")

#Approach 3
cat_age = int(input("Age: "))
if cat_age <= 6:
    print("Price is $250 for a kitten.")
if cat_age <= 11:
    print("Price is $225 for a teenager.")
if cat_age <= 95:
    print("Price is $150 for an adult.")
if cat_age >= 96:
    print("Price is $85 for a senior.")

#Approach 4
cat_age = int(input("Age: "))
if cat_age >= 96:
    print("Price is $85 for a senior.")
if cat_age <= 95:
    print("Price is $150 for an adult.")
if cat_age <= 11:
    print("Price is $225 for a teenager.")
if cat_age <= 6:
    print("Price is $250 for a kitten.")
#Task 2
#a) Aprroach #1 is the only one that works. 
#b)I think the difference is that one it has elif's after the first if so that they are all connected throughout the code.
# Two it goes from the lowest to the highest which causes it not to check the rest of the elif's if it already 
# triggered one of the elif's.