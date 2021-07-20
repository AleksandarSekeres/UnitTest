class Rick():
    def __init__(self, universe):
        self.universe= universe
        self.morty= None
        self.is_pickle= False

    def assign(self, morty):#assignovanje mortija ricku
        self.morty= morty
        morty.is_assigned= True

    