# Functions go here...
def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
        return "yes"

    elif response == "no" or response == "n":
        return "no"
 
    else:
      print("Please answer yes / no")

# checks that a number is between two values
def num_check(question, low, high) : 

    error = "Please enter an whole number between 1 and 10"

    vaild = False
    while not vaild:
        try:
            # ask the question
            response = int(input(question)) 

        
            # if the amount is too low / to high give
            if low < response <= high:
               return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes here...

print()
print("Welcome to the Lucky Unicorn Game")
print()

# ask user if they need instructions...
show_instructions = yes_no ( "have you played this game before ")

# If they say yes, output 'program continues'
if show_instructions == "no":
    print("show instructions")  # replace with instructions / call to instructions fnc


print()
how_much = num_check ("how much would you like to play with ", 0, 10)\

print("You will be spending $ {}".format(how_much))


 