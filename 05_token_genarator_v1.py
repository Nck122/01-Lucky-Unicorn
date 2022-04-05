import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop to generate 20 tokens

for item in range(0,100):

    chosen_num = random.randint(1, 100)

   

    #adjust balance

    if 1 <= chosen_num <= 4:

        chosen = "unicorn"

        balance += 4    

    elif 5 <= chosen_num <= 55:

        chosen = "donkey"

        balance -= 1

    else:

        if chosen_num % 2 == 0:

         chosen = "horse"

        else:

            chosen = "zebra"

        balance -= 0.5



    print("You got a {}. Your balance is "
      "${:.2f}".format(chosen, balance))
print()
