class Arrow(object):
    def __init__(self, theHero):
        self.x = theHero.x
        self.y = theHero.y
        self.speed = 30
    def update_me(self):
        self.x += self.speed
