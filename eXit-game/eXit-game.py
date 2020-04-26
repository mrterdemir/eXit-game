#  eXit version 1.2 | coded by Murat Erdemir | last update: 4/27/20

# # # # # # # # # # #
#      __  ___ _    #
#   ___\ \/ (_) |_  #
#  / _ \\  /| | __| #
# |  __//  \| | |_  #
#  \___/_/\_\_|\__| #
#                   #
# # # # # # # # # # #

# <<< main >>>

print("running eXit version 1.2")

# tutorial >>
print("\n\n<< TUTORIAL >>")
print("-"*50)
print("\nYou have 4 eligible answer for each phase, so you can pick one of these, then write the answer.")
print("If you choose wrong answer, you'll get the question back which is you answer it.\n")
print("-"*50)
print("\nHint:")
print("\nDid you watch the Sam Esmail's 'Mr. Robot' before?")
print("If you did, you can use the answers from S4-E11.")
print("Don't worry, there is no spoiler from Mr. Robot.\n")
print("-"*50)
print("\nAnswers: 'Examine', 'Interact', 'Leave', 'Stay'")
print("\nHint: 'Yes', 'No', 'Light', 'Take', 'Read' are eligible answers too.\n")
print("-"*50)

input("\nPRESS THE ENTER KEY TO START")

# answers >>

answer = ["leave", "stay", "examine", "light", "take", "read", "yes", "no"]
elliot_answer = ["move the barrel", "sit down next to my friend",
                 "enter tunnel", "stay", "light a match", "read note", "leave", "look", "get on the boat"]

# stages >>

print("\nYou're trapped in a dungeon with your friend.")    # Phase_1
print("You see a barrel. What do you do?")
while True:
    answer = input("> ").lower()
    if answer == "interact" or answer == "move the barrel":    # Phase_1.1 (Move the barrel)
        print("\nThe barrel rolls aside and you find a secret tunnel.")
        print("What do you do?")
        while True:
            answer = input("> ").lower()
            if answer == "interact" or answer == "leave" or answer == "enter tunnel":   # Phase_1.2 (Enter tunnel)
                print("\nYou start to escape but your friend is too weak to go with you.")
                print("They hand you a note.")
                print("What do you do?")
                while True:
                    answer = input("> ").lower()
                    if answer == "interact" or answer == "read" or answer == "take" or answer == "read note":
                        # Phase_1.3 (Read note)
                        print("\nIt is too dark to read the note.")
                        print("What do you do?")
                        while True:
                            answer = input("> ").lower()
                            if answer == "leave":   # Phase_1.4 (Leave)
                                print("\nYou crawl through the tunnel and the tunnel leads you to a beach.")
                                print("What do you do?")
                                while True:
                                    answer = input("> ").lower()
                                    if answer == "leave" or answer == "examine" or answer == "look":
                                        # Phase_1.5 (Look)
                                        print("\nIn the water you see a boat.")
                                        print("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "leave" or answer == "interact" or answer == "get on the boat":
                                                # Phase_1.6 (Get on the boat)
                                                print("\nCongratulations, you're heading to a new world!")
                                                input("\nPress enter to exit the game.")
                                                break
                                            elif answer == "stay":
                                                print("\nTunnel is collapsed, you cannot come back!")
                                                print("You left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                    elif answer == "stay":    # Phase_2.1 (Sit down next to my friend)
                                        print("\nYou came back! Your friend hands you a note.")
                                        print("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "interact" or answer == "take" or answer == "read" or answer == "stay":    # Phase_2.2 (Light a match)
                                                print("""\nThe note says, "Don't leave me here again." """)
                                                print("Do you leave your friend or stay?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "stay" or answer == "no":
                                                        print("\nDungeon is collapsed.")
                                                        print("You didn't left your friend.")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                            elif answer == "leave" or answer == "yes":
                                                print("\nYou left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                break
                            elif answer == "examine" or answer == "stay":    # Phase_2.1 (Sit down next to my friend)
                                print("\nYou found a match on the ground.")
                                print("Do you light the match?")
                                while True:
                                    answer = input("> ").lower()
                                    if answer == "interact" or answer == "light" or answer == "yes":
                                        # Phase_2.2 (Light a match)
                                        print("""\nThe note says, "Don't leave me here." """)
                                        print("Do you leave your friend or stay?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "stay" or answer == "no":
                                                print("\nDungeon is collapsed.")
                                                print("You didn't left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                            elif answer == "leave" or answer == "yes":
                                                print("\nYou left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                    elif answer == "leave" or answer == "no":
                                        print("\nYou crawl through the tunnel and the tunnel leads you to a beach.")
                                        input("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "leave" or answer == "examine" or answer == "look":
                                                print("\nIn the water you see a boat.")
                                                print("What do you do?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "leave" or answer == "interact" or answer == "get on the boat":
                                                        # Phase_1.6 (Get on the boat)
                                                        print("\nCongratulations, you're heading to a new world!")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                    elif answer == "stay":
                                                        print("\nTunnel is collapsed, you cannot come back!")
                                                        print("You left your friend.")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                            elif answer == "stay":
                                                print("\nYou came back! Your friend hands you a note.")
                                                print("What do you do?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "interact" or answer == "take" or answer == "read" or answer == "stay":
                                                        print("""\nThe note says, "Don't leave me here again." """)
                                                        print("Do you leave your friend or stay?")
                                                        while True:
                                                            answer = input("> ").lower()
                                                            if answer == "stay" or answer == "no":
                                                                print("\nDungeon is collapsed.")
                                                                print("You didn't left your friend.")
                                                                input("\nPress enter to exit the game.")
                                                                break
                                                        break
                                                    elif answer == "leave" or answer == "yes":
                                                        print("\nTunnel is collapsed, you cannot leave again!")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                        break
                                break
                        break
                    elif answer == "interact" or answer == "examine" or answer == "stay":
                        # Phase_2.1 (Sit down next to my friend)
                        print("\nDo you take the note?")
                        while True:
                            answer = input("> ").lower()
                            if answer == "interact" or answer == "stay" or answer == "yes":
                                # Phase_2.2 (Light a match)
                                print("""\nThe note says, "Don't leave me here." """)
                                print("Do you leave your friend or stay?")
                                while True:
                                    answer = input("> ").lower()
                                    if answer == "stay" or answer == "no":
                                        print("\nDungeon is collapsed.")
                                        print("You didn't left your friend.")
                                        input("\nPress enter to exit the game.")
                                        break
                                    elif answer == "leave" or answer == "yes":
                                        print("\nYou left your friend.")
                                        input("\nPress enter to exit the game.")
                                        break
                                break
                            elif answer == "leave" or answer == "no":
                                print("\nYou crawl through the tunnel and the tunnel leads you to a beach.")
                                print("What do you do?")
                                while True:
                                    answer = input("> ").lower()
                                    if answer == "leave" or answer == "examine" or answer == "look":
                                        print("\nIn the water you see a boat.")
                                        print("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "leave" or answer == "interact" or answer == "get on the boat":
                                                # Phase_1.6 (Get on the boat)
                                                print("\nCongratulations, you're heading to a new world!")
                                                input("\nPress enter to exit the game.")
                                                break
                                            elif answer == "stay":
                                                print("\nTunnel is collapsed, you cannot come back!")
                                                print("You left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                    elif answer == "stay":  # Phase_2.1 (Sit down next to my friend)
                                        print("\nYou came back! Your friend hands you a note.")
                                        print("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "interact" or answer == "take" or answer == "read" or answer == "stay":  # Phase_2.2 (Light a match)
                                                print("""\nThe note says, "Don't leave me here again." """)
                                                print("Do you leave your friend or stay?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "stay" or answer == "no":
                                                        print("\nDungeon is collapsed.")
                                                        print("You didn't left your friend.")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                            elif answer == "leave" or answer == "yes":
                                                print("\nTunnel is collapsed, you cannot leave again!")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                break
                        break
                break
            elif answer == "stay":
                print("\nYour friend hands you a note.")
                print("What do you do?")
                while True:
                    answer = input("> ").lower()
                    if answer == "interact" or answer == "take" or answer == "stay":
                        print("\nIt is too dark to read the note.")
                        print("What do you do?")
                        while True:
                            answer = input("> ").lower()
                            if answer == "examine" or answer == "stay":
                                print("\nYou found a match on the ground.")
                                print("Do you light the match?")
                                while True:
                                    answer = input("> ").lower()
                                    if answer == "interact" or answer == "light" or answer == "yes":
                                        # Phase_2.2 (Light a match)
                                        print("""\nThe note says, "Don't leave me here." """)
                                        print("Do you leave your friend or stay?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "stay" or answer == "no":
                                                print("\nDungeon is collapsed.")
                                                print("You didn't left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                            elif answer == "leave" or answer == "yes":
                                                print("\nYou left your friend.")
                                                input("\nPress enter to exit the game.")
                                                break
                                        break
                                    elif answer == "leave" or answer == "no":
                                        print("\nYou crawl through the tunnel and the tunnel leads you to a beach.")
                                        input("What do you do?")
                                        while True:
                                            answer = input("> ").lower()
                                            if answer == "leave" or answer == "examine" or answer == "look":
                                                print("\nIn the water you see a boat.")
                                                print("What do you do?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "leave" or answer == "interact" or answer == "get on the boat":
                                                        # Phase_1.6 (Get on the boat)
                                                        print("\nCongratulations, you're heading to a new world!")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                    elif answer == "stay":
                                                        print("\nTunnel is collapsed, you cannot come back!")
                                                        print("You left your friend.")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                            elif answer == "stay":
                                                print("\nYou came back! Your friend hands you a note.")
                                                print("What do you do?")
                                                while True:
                                                    answer = input("> ").lower()
                                                    if answer == "interact" or answer == "take" or answer == "read" or answer == "stay":
                                                        print("""\nThe note says, "Don't leave me here again." """)
                                                        print("Do you leave your friend or stay?")
                                                        while True:
                                                            answer = input("> ").lower()
                                                            if answer == "stay" or answer == "no":
                                                                print("\nDungeon is collapsed.")
                                                                print("You didn't left your friend.")
                                                                input("\nPress enter to exit the game.")
                                                                break
                                                        break
                                                    elif answer == "leave" or answer == "yes":
                                                        print("\nTunnel is collapsed, you cannot leave again!")
                                                        input("\nPress enter to exit the game.")
                                                        break
                                                break
                                        break
                                break
                        break
                    if answer == "interact" or answer == "stay":
                        print("""\nThe note says, "Don't leave me here." """)
                        print("Do you leave your friend or stay?")
                        while True:
                            answer = input("> ").lower()
                            if answer == "stay" or answer == "no":
                                print("\nDungeon is collapsed.")
                                print("You didn't left your friend.")
                                input("\nPress enter to exit the game.")
                                break
                        break
                    elif answer == "leave":
                        print("\nYou left your friend.")
                        input("\nPress enter to exit the game.")
                        break
                break
        break
    elif answer == "stay" or answer == "sit down next to my friend":    # Phase_2.1 (Sit down next to my friend)
        print("\nYour friend hands you a note.")
        print("What do you do?")
        while True:
            answer = input("> ").lower()
            if answer == "interact" or answer == "take" or answer == "read" or answer == "stay" or answer == "light a match":    # Phase_2.2 (Light a match)
                print("""\nThe note says, "Don't leave me here." """)
                print("Do you leave your friend or stay?")
                while True:
                    answer = input("> ").lower()
                    if answer == "stay" or answer == "no":
                        print("\nDungeon is collapsed.")
                        print("You didn't left your friend.")
                        input("\nPress enter to exit the game.")
                        break
                    elif answer == "leave" or answer == "yes":
                        print("\nYou left your friend.")
                        input("\nPress enter to exit the game.")
                        break
                break
            elif answer == "leave":
                print("\nYou left your friend.")
                input("\nPress enter to exit the game.")
                break
        break
    elif answer == "examine":
        print("\nThere is a light beam visible behind of the barrel.")
        print("What do you do?")
