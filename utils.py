from typing import List,Dict
import pandas as pd



# Define the quiz questions and answers
questions = [
       {
        "question": "How would you describe an alien whose favorite artist is Jcole, whose favorite car is a BMW X6, who dislikes Hypocrisy, and a last born?",
        "options": ["75% Lekan and 25% Muyiwa", "50% Lekan and 50% Semilore", "50% Joel and 50%Lekan", "75% Lekan and 25% Semilore"],
        "answer": "75% Lekan and 25% Semilore"
    },
    {
        "question": "How would you describe an alien who loves Truck!,loves tomike,loves Beans and rice, and lives in Lagos?",
        "options": ["50% Joel and 50% Tomi", "75% Joel and 25% Semilore", "100% Semilore", "50% Joel and 50% Semilore"],
        "answer": "50% Joel and 50% Semilore"
    },
    {
        "question": "How would you describe an alien who loves Asake and Fireboy, whose dream is to become a brand and marketing strategist, whose deal breaker is Cheating, and who studied Mass Communication?",
        "options": ["75% Tomi and 25% Semilore", "75% Tomi and 25% Lekan", "75% Monica and 25% Semilore", "100% Tomi"],
        "answer": "75% Tomi and 25% Semilore"
    },
    {
        "question": "How would you describe a child alien a.k.a Okanlawon, who is the third child,really loves an hyundai creta, and whose favorite food includes coleslaw?",
        "options": ["50% Monica and 50% Muyiwa", "75% Muyiwa and 25% Tomi", "50% Monica and 50% Tomi", "100% Monica"],
        "answer": "50% Monica and 50% Tomi"
    },
    {
        "question": "How would you describe an alien whose dream is to become a top ML Engineer, who loves Dunsin, BurnaBoy, and whose favourite color is red?",
        "options": ["100% Joel", "50% Joel and 50% Muyiwa", "75% Muyiwa and 25% Monica", "25% Joel and 75% Tomi"],
        "answer": "50% Joel and 50% Muyiwa"
    },
    {
        "question": "How would you describe an alien who loves Moses Bliss and Kizz Daniel, currently living a version of what's close to their dream, born in Ilorin and considers Infidelity a deal breaker?",
        "options": ["50% Monica and 50% Joel", "100% Monica","75% Monica and 25% Muyiwa", "25% Muyiwa and 75% Lekan"],
        "answer": "75% Monica and 25% Muyiwa"
    },
    {
        "question": "How would you describe an alien who consider low mentality a turn-off, who wants to drive a Mercedes G63S AMG, loves color white, and is the third child?",
        "options": ["50% Muyiwa and 50% Joel", "100% Muyiwa","75% Tomi and 25% Muyiwa", "75% Semilore and 25% Joel"],
        "answer": "75% Tomi and 25% Muyiwa"
    },
    {
        "question": "How would you describe an alien whose dream job is a sellside analyst, loves the color pink/army green, considers yeshua is favourite, and is the 4th child?",
        "options": ["75% Lekan and 25% Tomi", "75% Lekan and 25% Joel", "100% Joel", "25% Joel and 75% Lekan"],
        "answer": "75% Lekan and 25% Joel"
    },
    {
        "question": "How would you describe an alien who prefers Jollof rice beef and coleslaw, hates Unpleasant Smells, values Nursing, and loves the color red?",
        "options": ["75% Monica and 25% Joel", "100% Monica", "50% Tomi and 50% Monica", "25% Lekan and 75% Monica"],
        "answer": "75% Monica and 25% Joel"
    },
    {
        "question": "How would you describe a baby alien called  Sho Money, who would quit on an hypocrite, loves swallow alot and was born in Abeokuta?",
        "options": ["100% Semilore","50% Semilore and 50% Lekan", "75% Lekan and 25% Muyiwa", "25% Joel and 75% Lekan"],
        "answer": "50% Semilore and 50% Lekan"
    },
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
    
    
