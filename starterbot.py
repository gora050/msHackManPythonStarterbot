# Python startebot for MS. HACK-MAN challenge by urswego.
# Feel free to contact me via email: ursul@ucu.edu.ua (Vladyslav Ursul)
# Good luck!

class Field:
    '''
    Write your own field class
    '''
    def __init__(self, xsize, ysize):
        self.data = {}
        self.initialized = False
        self.xsize = xsize
        self.yxsize = ysize

    def update(self, field_str):
        '''
            Method for updating your field. Use self.initialized for
            optimizations
        '''
        if self.initialized:
            pass
        else:
            self.initialized = True


class Player:
    def __init__(self, p):
        self.name = p
        self.snippets = 0
        self.mines = 0

    def set(self, attr_name, value):
        if attr_name == "snippets":
            self.snippets = int(value)
        elif attr_name == "mines":
            self.mines = int(value)


class StarterBot:
    def __init__(self):
        self.data = {}
        self.field = None
        self.me = None
        self.round = 0

    def settings(self, args):
        '''
        args - list(str). Command splitted by spaces

        Saves all settings to self.data
        self.players - dict(Player.name : Player)
        Also link to your player in self.me
        '''
        self.data[args[0]] = args[1]
        if args[0] == "your_bot":
            self.players = dict(map(lambda x: (x, Player(x)),
                                    self.data["player_names"].split(",")))
            self.me = self.players[args[1]]

    def update(self, args):
        '''
        args - list(str). Command splitted by spaces
        '''
        if args[0] == "game":
            if args[1] == "field":
                '''
                update game field [c,…]
                CellType c (String)
                The current field, each coordinate separated by commas, from 
                top left to bottom right
                '''
                self.field.update()
            else:
                '''
                update game round i
                Number i (Integer)
                The current round (step).
                '''
                self.round = int(args[2])
        else:
            '''
            update p snippets i
            update p bombs i
            '''
            self.players[args[0]].set(args[1], args(2))

    def action(self, args):
        '''
        args - list(str). Command splitted by spaces
        '''
        if args[0] == "move":
            '''
            action move t
            Time t (Integer)
            Request for a direction to move. Should be answered within 
            t milliseconds.
            '''
            print("up")  # Write your movement strategy code here :)
        else:
            '''
            action character t
            Time t (Integer)
            Request for which character your bot would like to play as, only 
            asked at the start of the game. Should be answered within 
            t milliseconds.
            '''
            print("bixiette")

    def run(self):

        while 1:
            line = input()
            if len(line) == 0:
                continue
            parts = line.split(" ")
            controller = {
                "settings": self.settings,
                "update": self.update,
                "action": self.action
            }
            controller[parts[0]](parts[1:])


if __name__ == "__main__":
    Bot = StarterBot()
    Bot.run()
