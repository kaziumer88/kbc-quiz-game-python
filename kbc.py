print("🎉 Welcome to KBC (Kaun Banega Crorepati) 🎉")
print("-----------------------------------------------\n")

questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation?",
    "Which planet is known as the Red Planet?",
    "What is the national animal of India?"
]

options = [
    ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
    ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) Subhash Chandra Bose", "D) Bhagat Singh"],
    ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
    ["A) Lion", "B) Tiger", "C) Elephant", "D) Peacock"]
]

Answer = ["B","A","B","B"]

prize = 0

for i in range(len(questions)):
    print(f"Question{i+1}: {questions[i]}")

    for opt in options[i]:
        print(opt)

    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if(user_ans == Answer[i]):
          prize += 1000
          print(f"Correct! You Won the ₹{prize}\n")
    else:
        print("Wrong answer! Game Over.")
        print(f"You Take The Home ₹{prize}")
        break      

if prize == 4000:
    print("🎉 Congratulations! You answered all questions correctly! 🎉")
    print(f"🏆 Total Winning Amount: ₹{prize}")        