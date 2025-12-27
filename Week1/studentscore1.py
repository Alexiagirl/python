no_of_students = int(input("How many students are you inputting? "))
x = 0
while x < no_of_students:
    x = x + 1
    name = input("The name is? ")
    score = int(input("The score is? "))
    print ("The student's name is " + name + " and their score is " + str(score))
