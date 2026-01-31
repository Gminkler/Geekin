import random

class AdaptiveAITypeshi:
    def __init__(self):
        self.low = 1
        self.high = 100
        self.guess_history = []

    # Self is the current object here and ".append" adds one of the guesses to the list
    def make_guess(self):
        guess = (self.low + self.high)//2  # Binary Search Strategy
        self.guess_history.append(guess)  # tracks all of the guesses
        return guess
    
    def receive_feedback(self, feedback, guess):
        if feedback == "low":
            self.low = guess + 1
        elif feedback == "high":
            self.high = guess - 1

def play_game():
    print("Pick a number between 1 and 100. The AI will try to guess it!")
    target = int(input("Enter your number (The AI won't peek): "))

    ai = AdaptiveAITypeshi()
    turns = 0

    while True:
        guess = ai.make_guess()
        turns += 1
        print(f"AI guesses: {guess}")

        if guess == target:
            print(f"AI got it in {turns} turns!")
            break
        elif guess < target:
            ai.receive_feedback("low", guess)
        else:
            ai.receive_feedback("high", guess)

play_game()


