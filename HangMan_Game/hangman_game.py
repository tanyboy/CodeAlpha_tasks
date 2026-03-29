import random

# Step 1: Predefined words
words = ["java", "python", "apple", "table", "chair"]

# Step 2: Pick random word
word = random.choice(words)

# Step 3: Setup
guessed_word = ["_"] * len(word)
wrong_guesses = 0
max_wrong = 6
guessed_letters = []

# Step 4: Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:
    
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    guess = input("Enter a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    # Already guessed
    if guess in guessed_letters:
        print("Already guessed!")
        continue
    
    guessed_letters.append(guess)
    
    # Step 5: Check guess
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Step 6: Result
if "_" not in guessed_word:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
