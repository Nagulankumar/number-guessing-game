# 🎮 Number Guessing Game

A fun and interactive **Number Guessing Game** built with Python. Guess the secret number within limited attempts across 3 difficulty levels!

---

## 🕹️ How to Play

1. Choose a difficulty level (Easy / Medium / Hard)
2. The program picks a secret random number
3. You guess the number
4. The game gives you hints — Too High / Too Low / Hot / Cold
5. Guess correctly before attempts run out!

---

## 🎯 Difficulty Levels

| Level | Range | Attempts |
|-------|-------|----------|
| Easy | 1 – 50 | 10 |
| Medium | 1 – 100 | 7 |
| Hard | 1 – 200 | 5 |

---

## 🔥 Hint System

| Hint | Meaning |
|------|---------|
| 🔥 Very Hot | Within 5 numbers |
| ♨️ Hot | Within 15 numbers |
| 😐 Warm | Within 30 numbers |
| 🧊 Cold | More than 30 away |

---

## 🚀 How to Run

```bash
python number_guessing_game.py
```

---

## 📋 Sample Output

```
=============================================
       🎮 NUMBER GUESSING GAME 🎮
=============================================

Select Difficulty Level:
  1. Easy   → 1 to 50   (10 attempts)
  2. Medium → 1 to 100  (7 attempts)
  3. Hard   → 1 to 200  (5 attempts)

Enter choice: 2

🎯 Level    : Medium
📏 Range    : 1 to 100
🎲 Attempts : 7

Attempts left : 7
Enter your guess: 50
📈 Too Low! Guess HIGHER.  ♨️ Hot!

Attempts left : 6
Enter your guess: 75
🎉 CONGRATULATIONS! You guessed it!
```

---

## 👨‍💻 Author

**Nagulan**
AIML Engineering Student

---

## 📄 License

Open source under [MIT License](LICENSE).
