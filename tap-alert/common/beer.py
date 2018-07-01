class Beer:

    def __init__(self, name, brewery, style, abv):
        self.name = name
        self.brewery = brewery
        self.style = style
        self.abv = abv

    def __str__(self):
        return self.name + ' - ' + self.style + ' - ' + self.brewery + ' - ' + self.abv

    def sms(self):
        return f'{self.brewery}\n{self.name} - {self.abv}\n{self.style}\n'
