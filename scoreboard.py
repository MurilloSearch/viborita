import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.highscore = 0
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.highscore}',align='center')

    def increace_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()