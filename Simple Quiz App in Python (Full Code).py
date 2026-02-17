# Simple Quiz App in Python

def quiz_game():
    print("🎯 Welcome to the Quiz Game Bala!")
    print("----------------------------------")

    score = 0

    # Questions (List of Dictionaries)
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A) Chennai", "B) Delhi", "C) Mumbai", "D) Kolkata"],
            "answer": "B"
        },
        {
            "question": "2. Which language is used for Web Development?",
            "options": ["A) HTML", "B) Python", "C) Java", "D) All of these"],
            "answer": "D"
        },
        {
            "question": "3. What is the output of: 2 + 3 * 2?",
            "options": ["A) 10", "B) 7", "C) 8", "D) 6"],
            "answer": "B"
        },
        {
            "question": "4. Which company created Python?",
            "options": ["A) Google", "B) Microsoft", "C) Python Software Foundation", "D) Apple"],
            "answer": "C"
        }
    ]

    # Loop through questions
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! Correct Answer is:", q["answer"])

    # Final Result
    print("\n----------------------------------")
    print("🎉 Quiz Completed Bala!")
    print("Your Score:", score, "/", len(questions))

    if score == len(questions):
        print("🏆 Excellent! Full Marks!")
    elif score >= 2:
        print("👍 Good Job!")
    else:
        print("😅 Keep Practicing!")

# Run Quiz App
quiz_game()
