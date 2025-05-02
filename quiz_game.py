# Quiz Game

questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What language are we coding in?", "answer": "python"},
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ").strip().lower()
    
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {q['answer']}")

print(f"\nYou got {score} out of {len(questions)} correct.")
