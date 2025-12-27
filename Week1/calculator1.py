first_number = input("What is your first number? ")
second_number = input("What is your second number? ")
question = input("Division or Multiplication or Addition or Subtraction[+ or - or / or *] ")
if question == "Division" or question == "/":
    print (float(first_number) / float(second_number))
if question == "Multiplication" or question == "*":
    print (float(first_number) * float(second_number))
if question == "Addition" or question == "+":
    print (float(first_number) + float(second_number))
if question == "Subtraction" or question == "-":
    print (float(first_number) - float(second_number))