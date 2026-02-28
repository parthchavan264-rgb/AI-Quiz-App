# AI Quiz App - Master Version
# Author: Parth Chavan

import json
import os
import random

FILENAME = "quiz_data.json"

def load_quiz():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_quiz(quiz):
    with open(FILENAME, "w") as f:
        json.dump(quiz, f, indent=2)

def add_question(quiz):
    question = input("Enter quiz question: ")
    answer = input("Enter answer: ")
    hint = input("Enter hint: ")
    quiz[question] = {"answer": answer, "hint": hint}
    save_quiz(quiz)
    print("Question added successfully!")

def view_quiz(quiz):
    print("\n--- Quiz Questions ---")
    for q in quiz:
        print(f"Q: {q} | Answer: {quiz[q]['answer']} | Hint: {quiz[q]['hint']}")

def delete_question(quiz):
    question = input("Enter question to delete: ")
    if question in quiz:
        del quiz[question]
        save_quiz(quiz)
        print("Question deleted!")
    else:
        print("Question not found.")

quiz = load_quiz()

while True:
    print("\n1. Add Question")
    print("2. View Questions")
    print("3. Delete Question")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_question(quiz)
    elif choice == "2":
        view_quiz(quiz)
    elif choice == "3":
        delete_question(quiz)
    elif choice == "4":
        print("Exiting... Keep learning! 🚀")
        break
    else:
        print("Invalid choice. Try again.")
