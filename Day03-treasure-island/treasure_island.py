print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print(" you stand before the mountain path. It looks dangerous.")
choice1=input("Do you 'proceed' with the climb or 'retreat' to safety? ")
if choice1 == "proceed":
        print('''you are going to climb the mountain, Be aware of mountain lions!!
                As you are about to start your journey to the top of the mountain, 
                you see an old hermit,you stop as he was coming towards you
                He warns you: ' The journey is unpredictable. pack wisely.'***
                Before you can respond, he vanished into the mist.....  ''')
        choice2 = input("  do you want to keep some extra foods before start climbing?(y/n) ")
        choice3 = input("A mountain lion appears on the path! Do you want to 'freeze' or 'run'? " )
        if choice3 == "freeze":
            print("The lion looses interest and walks away. you continue safely.")
            choice4 = input("The path now splits into two routes: 'steep' shortcut or 'long' winding path. Which do you take? ")
            if choice4 == "long":
                print(" you take the safer route and avoid rockslides. you are getting closer!")
                choice5 = input(''' A storm approaches! Do you 'seek shelter' or 'keep climbing'? ''')
                if choice5 == "seek shelter":
                    if choice2 == "y":
                        print(" you wait out the storm safely in a cave. The path is now clear! ")
                    else:
                        print('''You wait out the storm in the cave, But due to lack of food you die of hunger.
                                                       "GAME OVER" ''')
                else:
                    print('''Lightning strikes nearby. you loose your footing. 
                                         "GAME OVER" ''')
            else:
                print(''' A rockslide blocks your path. you fall. 
                                 "GAME OVER" ''')

        else:
            print('''The lion chases you off a cliff. 
                           "GAME OVER" ''')

        print('''you finally reach the top of mountain
                   Suddenly....
              "A stone gate has appeared in front of you"
               when you go inside the it, the gate get closed ,
               you see 3 tunnels '1', '2', '3' ''')
        choice6 = int(input("Enter tunnel number: "))
        if choice6=="1":
            choice7 = int(input(''' A long bridge hangs over a sea of lava"
                            Enter a number to cross the bridge: '''))
            if choice7%2==0:
                print(" you safely reach outside the tunnel")
            else:
                print(''' you fall into lava.obviously you died.
                                "GAME OVER" ''')
        elif choice6 == "2":
            print(''' A monster blocks the tunnel!!''')
            choice8 = input(" First move- ' run towards it ' or ' throw a big rock '? ")
            if choice8 == "throw a big rock":
                print(" The rock hits! The monster is stunned.")
                choice9 = input("Now ' strike with sword ' or ' run past it '? ")
                if choice9=="run past it":
                    print(''' You escape while it's stunned! "VICTORY!!!" ''')
                else:
                    print('''It recovers too fast! 
                               "GAME OVER"  ''')
            else:
                print(''' The monster grabs you! 
                               "GAME OVER" ''')
        else:
            print('''  A MONSTER guards this tunnel! 
             It says: "Answer my riddle or face your death!" ''' )
            choice10 = input(' "What has keys but no locks?" Type your answer: ')
            if choice10 == "piano" or "keyboard":
                print(''' "correct!! The monster lets you pass." ''')
            else:
                print(''' "Wrong Answer! the monster attacks.
                                    "GAME OVER"  ''')
        print('''As you safely reach outside the gate , the ground started vibrating....      
                       "A BEHEMOTH HATH RISEN! STEP INTO THE RING 
                               FACE THE LIVING MOUNTAIN...
                                     THE GOLEM!!!" ''')

        fight= int(input("Enter a number to fight with the GOLEM"))
        if fight%2==0:
            print(''' "your attack hits the golem's weak spot!"
                       The golem stumbles... Cracks appear...
                       BOOM!! The golem Explodes into pieces! ''')
            print('''Congratulations! you have beaten the Mighty GOLEM :)
                     After the golem died, a key dropped, 
                     you see a treasure infront of you!!! ''')

            prize= int(input("Enter the SECRET CODE to unlock the treasure ('1','2' or '3' ): "))
            if prize==2:
             print('''         YEYYY!!!!!!!!!
                    "TREASURE HUNT SUCCCESSFULLY COMPLETED"
                            MISSION ACCOMPLISHED''')
            else:
                print(''' WRONG CODE! The treasure remains locked.
                          hahahaha... can't even unlock a treasure
                          you loose after coming at the end!! tch tch tch 
                          "A FOOL CAN NEVER GET THE TREASURE!!!!!!!!!!" ''')
        else:
            print(''' Your attack misses! The GOLEM crushes you.
                       "You lose the fight : GAME OVER :(" ''')
            
else:
    print(''' "You turned back. The treasure remains lost forever." 
                              "GAME OVER" ''')