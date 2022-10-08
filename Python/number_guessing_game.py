import random;

number = random.randint(1, 100);

print(".......... GUESS THE NUMBER ! ..........");
print("In this game you will have to guess the number that will lie between 1 & 100");
readyOrNot = input("So Are you ready ? (y/n) : ");

def Game() :
    previousGuessDistance = 0;
    turn = 0;
    while 1 :
        guess = int(input("Enter your guess : "));

        if guess == number :
            turn+=1;
            print("!!! YOU GOT IT !!!");
            print("SCORE : ", turn," | The lesser the better.");
            break;
        elif abs(guess-number) < previousGuessDistance :
            print("Congrat! you are closer");
            previousGuessDistance = abs(guess-number);
            turn+=1;
        else :
            if previousGuessDistance == 0 :
                print("Not the number .. try again ..");
                previousGuessDistance = abs(guess-number);
                turn+=1;
                continue;
            print("Ough! you went farther away");
            previousGuessDistance = abs(guess-number);
            turn+=1;


if readyOrNot == 'y' or readyOrNot == 'Y' :
    print("Great then Let's play");
    Game();
else :
    print("Doesn't matter .. Let's play anyways ;-)");
    Game();