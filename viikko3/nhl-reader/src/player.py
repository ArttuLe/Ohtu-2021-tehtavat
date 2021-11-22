class Player:
    def __init__(self, name,team,goals,assists,nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.points = goals+assists
    
    def __str__(self):
        return (f"{self.name:20}" f"{self.team:5}" f"{str(self.goals):3}" f"{'+':3}" f"{str(self.assists):3}" f"{'=':3}" f"{str(self.points)}" )
