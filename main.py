print("Welcome to my first game!")
name = input("What's your name? ")
age = int(input("How old are you? "))

health = 10

if age >= 18:
    print("Cool beans", name, ", you are old enough to play!")

    wants_to_play = input("Ready? ").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's go!")

        high_or_low = input("Do you take the high road or low road (high/low)? ")
        if high_or_low == "high":
            ans = input("Righteous! You reach a lake...swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side safely.")
            elif ans == "across":
                print("You managed to get across, but you were bit by a snake and lost 4 health.")
                health -= 4

            ans = input("You travel deeper into the woods and come across a house. Do you go inside or leave (inside/leave)? ")
            if ans == "inside":
                print("You go inside and are greeted by the owner...who is a crazyperson and tries to kill you!")
                health -= 6

                if health <= 0:
                    print("You now have 0 health and you lost the game. Buhbye.")
                else:
                    print("You have overpowered your enemy and are safe. You win!")

            else:
                print("You were eaten by wolves. Sorry! You were tasty, but you lose.")

        else:
            print("The road to hell is paved with good intentions. You lose.")

    else:
        print("Adios muchacho")
else:
    print("You are not old enough to play.")