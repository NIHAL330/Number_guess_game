print("NUMBER GUESSING GAME :)")
mo=0
while mo>=0:
    mo+=1
    lucky_numbers=902
    ne = int(input("enter your 3 digit lucky number:"))
    if ne==lucky_numbers:
        print("YOU WON :)")
        no=0
        while no>=0:
            man=input("PLAY AGAIN ('YES' or 'NO'):")
            if man=="YES":
                no+=1
                break
            elif man=="NO":
                print("GAME OVER")
                break
            else:
                print("invalid entry")
                no+=1
        if man=="NO":
            break
        else:
            continue
    else:
        print("YOU LOSS :(")
        print("enter yes to play again or no to quit")
        choice=input("enter your choice (YES or NO):")
        if choice=="YES":
            ne = int(input("enter your 3 digit lucky number:"))
            if ne == lucky_numbers:
                print("YOU WON :)")
                bo=0
                while bo>=0:
                    man = input("PLAY AGAIN ('YES' or 'NO'):")
                    if man == "YES":
                        mo += 1
                        break
                    elif man=="NO":
                        print("GAME OVER")
                        break
                    else:
                        print("invalid entry")
                        bo+=1
                if man=="NO":
                    break
                else:
                    continue
            else:
                print("YOU LOSS :(")
                print("enter yes to play again or no to quit")
                ko=0
                while ko<=0:
                    choice = input("enter your choice (YES or NO):")
                    if choice == "YES":
                        mo += 1
                        continue
                    elif choice == "NO":
                        print("GAME OVER")
                        break
                    else:
                        print("invalid entry")
                        ko+=1
                if choice=="NO":
                    break
                else:
                    continue
        elif choice=="NO":
            print("GAME OVER")
            break
        else:
            print("invalid entry")
            wow=input("do you want to continue or not(YES or NO):")
            if wow=="YES":
                continue
            elif wow=="NO":
                print("Game over")
                break
            else:
                print("invalid entry again game over")
                break