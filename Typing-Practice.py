import random
def main():
    phrases = []

    
    fileFound = False
    while not fileFound:
        chosenFile = input("Choose file in current directory to read from: ")
        try:
            with open(chosenFile, "r") as file:
                fileFound = True
                for line in file:
                    phrases.append(line.rstrip())
        except FileNotFoundError:
            print("No such file or directory")
    target = ""
    while not target.isdigit(): 
        target = input("Target Streak: ")
    target = int(target)
    streak = 0
    phrase = ""
    while streak < target:
        index = random.random()
        phrase = phrases[int((len(phrases) - 1) * index)]
        answer = input(phrase + " Streak: " + str(streak) + " ")
        if answer == phrase:
            streak += 1
        else:
            streak = 0

    print("Reached " + str(target) + " streak!")

if __name__ == "__main__":
    main()