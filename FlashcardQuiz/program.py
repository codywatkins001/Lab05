from services import flashcardloader
from services import quizengine

def main():
    file_path = "data/flashcards.json"
    flashcards = FlashcardLoader.load(file_path)

    if not flashcards:
        print("No flashcards loaded. Exiting...")
        return

    quiz = QuizEngine(flashcards)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
