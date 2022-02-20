class Baseclass:  
    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)
