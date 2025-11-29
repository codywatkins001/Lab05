import json
from models import flashcard

class FlashcardLoader:

    @staticmethod
    def load(file_path: str):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            return [Flashcard(item["question"], item["answer"]) for item in data]

        except FileNotFoundError:
            print("Flashcards file not found.")
            return []
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            return []
