import random
lst = ["Stone" , "Paper" , "Scissors"]
mood = input("Do you want to play:")
if mood.upper() == "YES":
    play = True
while play is True:

    Your_Choice = input("Enter your Choice from (Stone , Paper , Scissor)")
    Computer_Choice = random.choice(lst)
    if Your_Choice.upper() == "STONE" and Computer_Choice.upper() == "PAPER":
        print(f"YOU LOSE\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "STONE" and Computer_Choice.upper() == "SCISSOR":
        print(f"YOU WIN\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "STONE" and Computer_Choice.upper() == "STONE":
        print(f"DARW\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "PAPER" and Computer_Choice.upper() == "PAPER":
        print( f"DARW\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "PAPER" and Computer_Choice.upper() == "STONE":
        print( f"YOU WIN\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "PAPER" and Computer_Choice.upper() == "SCISSOR":
        print( f"YOU LOSE\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "SCISSOR" and Computer_Choice.upper() == "PAPER":
        print( f"YOU WIN\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "SCISSOR" and Computer_Choice.upper() == "STONE":
        print( f"YOU LOSE\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "SCISSOR" and Computer_Choice.upper() == "SCISSOR":
        print( f"DRAW\nYOUR CHOICE:{Your_Choice} and COMPUTER CHOICE:{Computer_Choice}")
    elif Your_Choice.upper() == "EXIT":
        break
    else:
        print("INVALID CHOICE")
        