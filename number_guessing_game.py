# ============================================================
# Number Guessing Game
# Author : Nagulan
# Description: Guess the secret number within limited attempts
# ============================================================

import random

def display_welcome():
    print("=" * 45)
    print("       🎮 NUMBER GUESSING GAME 🎮")
    print("=" * 45)

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("  1. Easy   → 1 to 50   (10 attempts)")
    print("  2. Medium → 1 to 100  (7 attempts)")
    print("  3. Hard   → 1 to 200  (5 attempts)")

    while True:
        choice = input("\nEnter choice (1 / 2 / 3): ").strip()
        if choice == "1":
            return 1, 50, 10, "Easy"
        elif choice == "2":
            return 1, 100, 7, "Medium"
        elif choice == "3":
            return 1, 200, 5, "Hard"
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def give_hint(guess, secret):
    difference = abs(guess - secret)
    if difference == 0:
        return ""
    elif difference <= 5:
        return "🔥 Very Hot! Extremely close!"
    elif difference <= 15:
        return "♨️  Hot! You are close!"
    elif difference <= 30:
        return "😐 Warm. Getting closer."
    else:
        return "🧊 Cold. Very far away."

def play_game():
    display_welcome()

    low, high, max_attempts, level = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts_left = max_attempts
    guessed_numbers = []

    print(f"\n🎯 Level    : {level}")
    print(f"📏 Range    : {low} to {high}")
    print(f"🎲 Attempts : {max_attempts}")
    print("\nGood luck! Start guessing...\n")

    while attempts_left > 0:
        print(f"Attempts left : {attempts_left}")
        print(f"Your guesses  : {guessed_numbers if guessed_numbers else 'None yet'}")

        try:
            guess = int(input(f"Enter your guess ({low} - {high}): "))
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            continue

        if guess < low or guess > high:
            print(f"⚠️  Out of range! Guess between {low} and {high}.\n")
            continue

        if guess in guessed_numbers:
            print("⚠️  You already guessed that number! Try a different one.\n")
            continue

        guessed_numbers.append(guess)
        attempts_left -= 1

        if guess == secret_number:
            attempts_used = max_attempts - attempts_left
            print("\n" + "=" * 45)
            print(f"🎉 CONGRATULATIONS! You guessed it!")
            print(f"✅ Secret Number  : {secret_number}")
            print(f"🎯 Attempts Used  : {attempts_used} / {max_attempts}")
            if attempts_used == 1:
                print("🏆 PERFECT SCORE! First try!")
            elif attempts_used <= max_attempts // 2:
                print("⭐ Excellent performance!")
            else:
                print("👍 Well done!")
            print("=" * 45)
            return True

        # Give directional hint
        direction = "📈 Too Low!  Guess HIGHER." if guess < secret_number else "📉 Too High! Guess LOWER."
        hint = give_hint(guess, secret_number)
        print(f"{direction}  {hint}\n")

    # Game over
    print("\n" + "=" * 45)
    print("💀 GAME OVER! You ran out of attempts.")
    print(f"🔐 The secret number was : {secret_number}")
    print("=" * 45)
    return False

def main():
    while True:
        play_game()
        again = input("\n🔄 Play again? (yes / no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\n👋 Thanks for playing! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
