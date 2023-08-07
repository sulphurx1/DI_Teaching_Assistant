import random

# Exercise 2

def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Alice in Wonderland")

# Exercise 3

def describe_city(city, country):
    print(city + " is in " + country)

describe_city("Reykjavik", "Iceland")

# Exercise 4

def number_comparator():
    inputNumber = int(input("Please enter a number from 1 to 100: "))
    if inputNumber < 1 or inputNumber > 100:
        print("The number you have entered is out of range\nPlease try again")
        number_comparator()
    else:
        randomNumber = random.randint(1, 100)
        if inputNumber == randomNumber:
            print("The number you have entered is the same as the random number")
        elif inputNumber > randomNumber:
            print("The input number is greater than the random number")
        elif inputNumber < randomNumber:
            print("The input number is less than the random number")

number_comparator()

# Exercise 5

def make_shirt(size = "Large", text = "I love Python"):
    if size.lower() in ["small", "medium", "large"]:
        print(f"The size of the shirt is {size} and the text is {text}.")
    else: 
        print("Invalid size")

make_shirt()
make_shirt("Medium")
make_shirt("Small", "I dont like Python")

# Exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)


def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = "The Great " + magician_names[i]

show_magicians()
make_great()
show_magicians()

# Exercise 7

def get_random_temp(season):
    if season.lower() == "winter":
        return random.randint(-10, 16)
    elif season.lower() == "fall":
        return random.randint(17, 22)
    elif season.lower() == "spring":
        return random.randint(23, 30)
    elif season.lower() == "summer":
        return random.randint(31, 40)
    
# Bonus 5
def get_random_temp_floating(season):
    if season.lower() == "winter":
        return random.uniform(-10.0, 16.0)
    elif season.lower() == "fall":
        return random.uniform(17.0, 22.0)
    elif season.lower() == "spring":
        return random.uniform(23.0, 30.0)
    elif season.lower() == "summer":
        return random.uniform(31.0, 40.0)

def main(season):
    temperature = get_random_temp_floating(season)
    print(f"The temperature right now is {temperature} degress Celsius")
    if temperature < 0 :
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif temperature >= 0 and temperature <= 16:
        print(f"Quite chilly! Don’t forget your coat")
    elif temperature >= 16 and temperature <= 23:
        print("Normal")
    elif temperature >= 23 and temperature <= 32:
        print("Very Hot")
    elif temperature >= 32 and temperature <= 40:
        print("Volcano")
    
season = input("Please enter a season: ")
main(season)

# Exercise 5

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

    
def ask_question():
    correctAns = 0 
    wrongAns = 0

    wrong_answers = []

    def information_desk():
        print(f"Correct Answer: {correctAns}\nWrong Answer: {wrongAns}")

    if wrongAns > 3:
        print("Game Over!")
        z = input("Press 1 to re try again")
        
        if int(z) == 1:
            ask_question()

    else:
        for question in data:
            x = input(question["question"])

            if question["answer"] == x:
                correctAns += 1

                information_desk()

            else:
                wrong_answers.append(x)
                wrongAns += 1

                print("Correct Answer was :" + question["answer"] + "\n What you answered with: " + x)

                information_desk()
ask_question()



    