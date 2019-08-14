class GameField(object):
    def __init__(self, left_edge, right_edge, top_edge, bot_edge):
        self.__left_edge = left_edge
        self.__right_edge = right_edge
        self.__top_edge = top_edge
        self.__bot_edge = bot_edge

        self.__snake = None
        self.__food = None
        self.__score = 0
    
    @property
    def left_edge(self):
        return self.__left_edge

    @property
    def right_edge(self):
        return self.__right_edge

    @property
    def top_edge(self):
        return self.__top_edge

    @property
    def bot_edge(self):
        return self.__bot_edge

    @property
    def score(self):
        return self.__score

    @property
    def snake(self):
        return self.__snake

    def add_snake(self):
        pass