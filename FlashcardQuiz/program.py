from services.flashcardloader import flashcardLoader
from services.quizengine import quizengine

def main():
    file_path = "data/flashcards.json"
    flashcards = load(file_path)

    if not flashcards:
        print("No flashcards loaded. Exiting...")
        return

    quiz = quizengine(flashcards)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
