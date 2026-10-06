import random
def main():
    phrases = []
    with open("phrases.txt", "r") as file:
        for line in file:
            phrases.append(line)
                   
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