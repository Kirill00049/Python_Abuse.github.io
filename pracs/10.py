class MealyError(Exception):
    pass


class Milya:
    state = "A"

    def reset(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 1
        elif self.state == "C":
            self.state = "D"
            return 2
        elif self.state == "D":
            self.state = "E"
            return 3
        elif self.state == "E":
            return 6
        else:
            return 7

    def mute(self):
        if self.state == "D":
            self.state = "A"
            return 4
        elif self.state == "E":
            self.state = "F"
            return 5
        elif self.state == "F":
            self.state = "B"
            return 8
        else:
            raise MealyError("mute")


def test():
    o = main()
    try:
        o.mute()
    except MealyError:
        pass
    o.reset()
    try:
        o.mute()
    except MealyError:
        pass
    o.reset()
    try:
        o.mute()
    except MealyError:
        pass
    o.reset()
    o.mute()
    o.reset()
    o.reset()
    o.reset()
    o.reset()
    o.reset()
    o.mute()
    o.reset()
    o.mute()
    o.reset()
    o.reset()
    o.mute()
    o.reset()
    o.reset()
    o.reset()
    o.reset()
    o.mute()
    o.mute()


def main():
    o = Milya()
    return o


test()

