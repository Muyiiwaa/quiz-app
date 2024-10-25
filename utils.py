from typing import List,Dict
import psycopg2
import pandas as pd



# Define the quiz questions and answers
questions = [
    {
        "question": "Become a husband first",
        "options": ["Joel", "Lekan", "Muyiwa"],
        "answer":"Joel"
    },
    {
        "question": "Become a wife first",
        "options": ["Monica", "Semilore", "Tomisin"],
        "answer":"Monica"
    },
    {
        "question": "Say 'I love you' to their partner the most",
        "options": ["Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"],
        "answer":"Tomi"
    },
    {
        "question": "The clingy couple?",
        "options": ["Tomi and Muyiwa", "Joel and Monica", "Lekan and Semilore"],
        "answer":"Tomi and Muyiwa"
    },
    {
        "question": "Become a movie star",
        "options": ["Lekan", "Tomi", "Joel", "Muyiwa", "Semilore", "Monica"],
        "answer":"Tomi"
    },
    {
        "question": "Eat the most food at a gathering",
        "options": ["Lekan", "Tomi", "Semilore", "Muyiwa", "Joel", "Monica"],
        "answer":"Lekan"
    },
    {
        "question": "Get fat when life gets more comfortable",
        "options": ["Monica/Muyiwa", "Semilore/Monica", "Lekan/Muyiwa", "Joel/Lekan", "Tomi/Joel", "Monica/Lekan"],
        "answer":"Joel/Lekan"
    },
    {
        "question": "Get caught drunk",
        "options": ["Monica", "Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"],
        "answer":"Semilore"
    },
    {
        "question": "Try to joke their way out of trouble",
        "options": ["Lekan", "Tomi", "Joel", "Semilore", "Muyiwa", "Monica"],
        "answer":"Joel"
    },
    {
        "question": "Buy something they can't pay for and run away",
        "options": ["Monica", "Semilore", "Muyiwa", "Joel", "Tomi", "Lekan"],
        "answer":"Lekan"
    },
    {
        "question": "Get in a fist fight",
        "options": ["Monica", "Joel", "Semilore", "Tomi", "Lekan", "Muyiwa"],
        "answer":"Joel"
    },
    {
        "question": "Who is the best cook?",
        "options": ["Monica", "Muyiwa", "Tomi", "Joel", "Lekan", "Semilore"],
        "answer":"Monica"
    },
    {
        "question": "Who is the most reserved?",
        "options": ["Muyiwa", "Monica", "Tomi", "Joel", "Lekan", "Semilore"],
        "answer":"Monica"
    },
    {
        "question": "Who is the fixer?",
        "options": ["Semilore", "Monica", "Muyiwa", "Tomi", "Lekan", "Joel"],
        "answer":"Lekan"
    },
    {
        "question": "Who is the life of the party?",
        "options": ["Semilore", "Muyiwa", "Tomi", "Monica", "Lekan", "Joel"],
        "answer":"Tomi"
    },
    {
        "question": "Who is the funniest?",
        "options": ["Tomi/Joel", "Tomi/Muyiwa", "Lekan/Tomi", "Muyiwa/Joel", "Lekan/Joel", "Muyiwa/Lekan"],
        "answer":"Muyiwa/Joel"
    },
    {
        "question": "Who is the best dancer?",
        "options": ["Muyiwa/Semilore", "Monica/Lekan", "Joel/Monica", "Tomi/Semilore", "Joel/Lekan", "Monica/Semilore"],
        "answer":"Tomi/Semilore"
    },
    {
        "question": "Who comes off as the bookworm?",
        "options": ["Monica", "Muyiwa", "Tomi", "Semilore", "Joel", "Lekan"],
        "answer":"Muyiwa"
    },
    {
        "question": "Who is the smartest?",
        "options": ["Monica", "Lekan", "Joel", "Muyiwa", "Semilore", "Tomi"],
        "answer":"Muyiwa"
    },
    {
        "question": "Who is the clumsiest?",
        "options": ["Lekan", "Muyiwa", "Monica", "Semilore", "Tomi", "Joel"],
        "answer":"Semilore"
    },
    {
        "question": "Who is the most fashionable?",
        "options": ["Monica", "Muyiwa", "Semilore", "Lekan", "Joel", "Tomi"],
        "answer":"Semilore"
    },
    {
        "question": "Who is the most spiritual?",
        "options": ["Monica/Joel", "Muyiwa/Joel", "Tomi/Lekan", "Semilore/Joel", "Joel/Lekan", "Monica/Semilore"],
        "answer":"Semilore/Joel"
    },
    {
        "question": "Who looks like they snore the loudest?",
        "options": ["Monica", "Lekan", "Joel", "Muyiwa", "Semilore", "Tomi"],
        "answer":"Lekan"
    },
    {
        "question": "Who is the most caring?",
        "options": ["Lekan", "Muyiwa", "Monica", "Semilore", "Tomi", "Joel"],
        "answer":"Joel"
    },
    {
        "question": "Who is the glutton?",
        "options": ["Monica", "Muyiwa", "Semilore", "Lekan", "Joel", "Tomi"],
        "answer":"Lekan"
    }
]

real_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "F. Scott Fitzgerald", "Mark Twain", "Ernest Hemingway"],
        "answer": "Harper Lee"
    }
]

def get_questions(inputs:List = questions) -> List[Dict]:
    return inputs



if __name__ == "__main__":
    print(len(real_questions))