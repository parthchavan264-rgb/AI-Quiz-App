# AI Quiz App - Master Version
# Author: Parth Chavan

import json
import os
import random

FILENAME = "quiz_data.json"

# Load quiz data from JSON
def load_quiz():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

# Save quiz data to JSON
def save_quiz(quiz):
    with open(FILENAME, "w") as f:
        json.dump(quiz, f, indent=2)

# Add a new quiz question
def add_question(quiz):
    question = input("Enter quiz question: ")
    if question in quiz:
        print("Question already exists!")
        return
    answer = input("Enter answer: ")
    hint = input("Enter hint: ")
    quiz[question] = {"answer": answer, "hint": hint}
    save_quiz(quiz)
    print("Question added successfully!")

# View all quiz questions
def view_quiz(quiz):
    print("\n--- Quiz Questions ---")
    if not quiz:
        print("No questions added yet.")
        return
    for q in quiz:
        print(f"Q: {q} | Answer: {quiz[q]['answer']} | Hint: {quiz[q]['hint']}")

# Delete a question
def delete_question(quiz):
    question = input("Enter question to delete: ")
    if question in quiz:
        del quiz[question]
        save_quiz(quiz)
        print("Question deleted!")
    else:
        print("Question not found.")

# Edit an existing question
def edit_question(quiz):
    question = input("Enter question to edit: ")
    if question in quiz:
        new_answer = input("Enter new answer: ")
        new_hint = input("Enter new hint: ")
        quiz[question] = {"answer": new_answer, "hint": new_hint}
        save_quiz(quiz)
        print("Question updated!")
    else:
        print("Question not found.")

# Main CLI
quiz = load_quiz()

while True:
    print("\n--- AI Quiz App ---")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Edit Question")
    print("4. Delete Question")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_question(quiz)
    elif choice == "2":
        view_quiz(quiz)
    elif choice == "3":
        edit_question(quiz)
    elif choice == "4":
        delete_question(quiz)
    elif choice == "5":
        print("Exiting... Keep learning and building! 🚀")
        break
    else:
        print("Invalid choice. Please enter a number between 1-5.")
