import random                                                          # Imports the random module
import time                                                            # Imports the time module

active = True                                                          # For the while loop later on

answers = \
    ["As I see it, yes.",
     "Ask again later.",
     "Better not tell you now.",
     "Cannot predict now.",
     "Concentrate and ask again",
     "Don’t count on it.",
     "It is certain.",
     "It is decidedly so.",
     "Most likely.",
     "My reply is no.",
     "My sources say no.",
     "Outlook not so good.",
     "Outlook good.",
     "Reply hazy, try again.",
     "Signs point to yes.",
     "Very doubtful.",
     "Without a doubt.",
     "Yes.",
     "Yes – definitely.",
     "You may rely on it.",
     ]

while active:                                                          # This section will repeat until manually exited
    question = input("\nPlease ask a question or type exit to quit...\n")   # To check what the user wants to do

    if question.lower() == "exit":                                     # If user wants to exit, run the code below
        exit()                                                         # Exits the programme
    elif question.find("?") == -1:                                     # If input doesn't contain a ? run the code below
        print("That is not a question, please try again")              # Inform user that they have not asked a question
    else:
        response = random.randint(1, 20)                               # If both if statements are satisfied
        print("thinking...")
        time.sleep(3)                                                  # To give impression programme is thinking
        print(answers[response])
