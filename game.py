import random

class Game:
    def __init__(self, questions):
        self.questions = questions
        self.options = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.current_question = 0

    def rps_round(self):
        player_action = input("Enter a choice (rock, paper, scissors): ")
        if player_action not in self.options:
            print("Invalid choice, try again.")
            return
        computer_action = random.choice(self.options)
        print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")
        if player_action == computer_action:
            print("It's a tie!")
        elif (player_action == "rock" and computer_action == "scissors") or \
             (player_action == "paper" and computer_action == "rock") or \
             (player_action == "scissors" and computer_action == "paper"):
            print("You win this round!")
            self.player_score += 1
            if self.current_question < len(self.questions):
                self.quiz_question()
        else:
            print("Computer wins this round!")
            self.computer_score += 1

    def quiz_question(self):
        if self.current_question >= len(self.questions):
            print("You have answered all the quiz questions, game over!")
            print(f"The winner is {self.player_score if self.player_score > self.computer_score else 'Computer'}")
            print(f"Your final score: {self.player_score}, Computer final score: {self.computer_score}")
            return
        question, correct_answer = self.questions[self.current_question]
        answer = input(question + " (True or False): ")
        if answer.lower() == "true":
            player_answer = True
        elif answer.lower() == "false":
            player_answer = False
        else:
            print("Invalid answer, try again.")
            return
        if player_answer == correct_answer:
            print("Correct!")
            self.current_question += 1
        else:
            print("Incorrect!")
            self.computer_score += 1
        print(f"Score: You {self.player_score}, Computer {self.computer_score}")

class Quiz(Game):
    def __init__(self, questions):
        super().__init__(questions)

if __name__ == "__main__":
    questions = [
        ("The Prince of Wales' full name is William Arthur Philip Louis Mountbatten-Windsor.", True),
        ("Titan is the largest moon of Saturn.", True),
        ("Vin Diesel only acted on 3 of the Fast and Furious franchise.",False),
        ("The first computer was invented in 1947.",False),
        ("In 1958, the first Lego brick was invented.",True),
        ("The oldest tree in the world is in Sacramento.",False),
        ("Vehicles from Morocco use the international registration letter MA",True),
        ("The knight chess piece can move in a straight line.",False),
        ("Nauru is the smallest country in the world",False),
        ("Athena is the greek goddess of wisdom and warfare.",True),
        ("The ancient city of Machu Picchu is in Puerto Rico.",False),
        ("Juventus football team is from Spain.",False),
        ("Ca is the chemical symbol of calcium.",True),
        ("Pablo Picasso painted the famous artwork The Birth Of Venus.",False),
        ("Algeria is the largest nation in Africa.",True),
    ]
    game = Quiz(questions)
    while True:
        game.rps_round()
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
             break