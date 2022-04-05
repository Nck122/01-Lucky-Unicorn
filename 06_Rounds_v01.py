# set the balance for testing purposes
from asyncio import run_coroutine_threadsafe


balance = 5 

rounds_played = 0


play_again = input ("Press <Enter> to play...")
while play_again == "":


    # increases # of rounds played
    rounds_played += 1 

    # Print round number
    print("*** Rounds #{} ***".format(rounds_played))
    balance -= 1 
    print("Balance: ", balance)
    print()

    
    play_again = input("Press Enter to play again" "or 'xxx' to quit ")

