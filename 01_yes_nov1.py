# Functions go here...
def yes_no (question):
  valid = False
  while not valid:
    response = input ( "Have you played this game before? "). lower()

    if response == "yes" or response == "y":
        return "yes"

    elif response == "no" or response == "n":
        return "no"
 
    else:
      print("Please answer yes / no")

# Main Routine goes here...
show_instructions = ""
while show_instructions.lower () != "xxx":

    # Ask the user if they have played before



    show_instructions = input ( "have you played this game before "). lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print ("program continues")


    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print ("display instructions")


