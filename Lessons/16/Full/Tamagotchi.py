class Tamagotchi:
    def __init__(self):
        self.poziom_glodu = 50
        self.poziom_szczescia = 50
    
    def nakarm(self):
        self.poziom_glodu += 10

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        
    def aktualizuj(self):
        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1