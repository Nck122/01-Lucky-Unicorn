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
print("Game continues...")


 