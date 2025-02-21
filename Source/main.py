import turtle
import random

# Word list for the game (filtered to exclude inappropriate words)
WORDS = [
    "apple", "grape", "mango", "peach", "lemon", "berry", "cherry", "melon", "plums", "pears",
    "apron", "baker", "candy", "dance", "eagle", "fable", "giant", "happy", "ideal", "jolly",
    "karma", "lemon", "magic", "noble", "ocean", "piano", "queen", "robot", "sunny", "tiger",
    "uncle", "vivid", "witty", "xenon", "yacht", "zebra", "adore", "brave", "charm", "dream",
    "eager", "fancy", "globe", "honor", "image", "jewel", "knack", "lucky", "mirth", "nifty",
    "olive", "pride", "quilt", "raven", "smile", "trust", "unity", "vigor", "whale", "xenon",
    "youth", "zesty", "actor", "beach", "crane", "dough", "elbow", "flame", "grill", "house",
    "input", "jumpy", "kneel", "latch", "mover", "nurse", "orbit", "pouch", "quack", "rider",
    "scent", "tough", "ultra", "vocal", "wrist", "xerox", "yield", "zonal", "abide", "blaze",
    "climb", "dwarf", "frost", "glide", "haste", "inbox", "jolly", "knock", "lunar", "mirth",
    "noble", "oasis", "piano", "quilt", "raven", "smile", "trust", "unity", "vigor", "whale",
    "xenon", "youth", "zesty", "actor", "beach", "crane", "dough", "elbow", "flame", "grill",
    "house", "input", "jumpy", "kneel", "latch", "mover", "nurse", "orbit", "pouch", "quack",
    "rider", "scent", "tough", "ultra", "vocal", "wrist", "xerox", "yield", "zonal", "abide",
    "blaze", "climb", "dwarf", "frost", "glide", "haste", "inbox", "jolly", "knock", "lunar",
    "mirth", "noble", "oasis", "piano", "quilt", "raven", "smile", "trust", "unity", "vigor",
    "whale", "xenon", "youth", "zesty", "actor", "beach", "crane", "dough", "elbow", "flame",
    "grill", "house", "input", "jumpy", "kneel", "latch", "mover", "nurse", "orbit", "pouch",
    "quack", "rider", "scent", "tough", "ultra", "vocal", "wrist", "xerox", "yield", "zonal"
    "hello", "world", "python", "turtle", "wordle", "happy", "smile", "laugh", "funny", "jolly"
    
]
SECRET_WORD = random.choice(WORDS)
ATTEMPTS = 6
WORD_LENGTH = len(SECRET_WORD)

turtle.setup(500, 500)
turtle.title("Turtle Wordle")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_board():
    t.clear()
    t.penup()
    start_x, start_y = -100, 200
    for i in range(ATTEMPTS):
        for j in range(WORD_LENGTH):
            t.goto(start_x + j * 40, start_y - i * 50)
            t.pendown()
            t.forward(30)
            t.penup()

def display_guess(guess, row):
    start_x, start_y = -95, 180 - row * 50
    for i, letter in enumerate(guess):
        t.goto(start_x + i * 40, start_y)
        if letter == SECRET_WORD[i]:
            t.color("green")
        elif letter in SECRET_WORD:
            t.color("orange")
        else:
            t.color("gray")
        t.write(letter, align="left", font=("Arial", 18, "bold"))
    t.color("black")

def main():
    draw_board()
    attempts = 0
    print("Welcome to Turtle Wordle! Can You Guess The Word?")
    
    while attempts < ATTEMPTS:
        guess = input("Enter Your Guess: ").lower()
        if len(guess) != WORD_LENGTH or guess not in WORDS:
            print("Sorry! I Think That Was An Invalid Guess. Can You Please Try Again?")
            continue
        
        display_guess(guess, attempts)
        if guess == SECRET_WORD:
            print("Congratulations! You Have Guessed The Word And Beat Turtle Wordle!")
            break
        attempts += 1
    else:
        print(f"Game over! Just To Know, The Word Was {SECRET_WORD}")
    
    turtle.done()

if __name__ == "__main__":
    main()