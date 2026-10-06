import random
def main():

    phrases = ["[]", "()", "{}", "([x])", "{x}", "(x)", "function(variable)", "dictionary[index]", "3 < 7", "7 > 3"]

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