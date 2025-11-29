import json
from models import flashcard

class flashcardLoader:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            return [flashcard(item["question"], item["answer"]) for item in data]

        except FileNotFoundError:
            print("Flashcards file not found.")
            return []
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            return []
