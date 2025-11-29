class QuizEngine:
    def __init__(self, cards):
        self.cards = cards

    def run_quiz(self):
        print("\n--- Flashcard Quiz ---\n")
        correct = 0

        for card in self.cards:
            print(f"Q: {card.question}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == card.answer.lower():
                print("Correct!\n")
                correct += 1
            else:
                print(f"Incorrect. The correct answer is: {card.answer}\n")

        print(f"Quiz complete! Score: {correct}/{len(self.cards)}")
