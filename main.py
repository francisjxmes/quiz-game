quiz_questions = [
  {"question": "What is the capital of Canada?", "answer": "ottawa"},
  {"question": "Which river flows through Cairo?", "answer": "nile"},
  {"question": "What country has the most natural lakes?", "answer": "canada"},
  {"question": "Who played Iron Man in the Marvel Cinematic Universe?", "answer": "robert downey jr"},
  {"question": "What is the name of the Netflix series featuring a chess prodigy named Beth Harmon?", "answer": "the queen's gambit"},
  {"question": "Which artist released the hit song 'Bad Guy' in 2019?", "answer": "billie eilish"},
  {"question": "Who is the current president of the United States?", "answer": "donald trump"},
  {"question": "Which country exited the European Union in 2020?", "answer": "united kingdom"},
  {"question": "What international organization is abbreviated as 'UN'?", "answer": "united nations"}
]


def run_quiz():
    score = 0  # start at 0

    for q in quiz_questions:
        user_answer = input(q["question"] + " ").strip().lower()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer'].title()}\n")

    print(f"You got {score} out of {len(quiz_questions)} correct.")

# Start the quiz
run_quiz()
