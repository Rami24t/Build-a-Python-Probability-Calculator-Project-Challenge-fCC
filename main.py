import copy
import random


class Hat():
    def __init__(self, **kwargs):
        self.count = kwargs
        self.contents = Counter.spread(**kwargs)

    def __str__(self):
        params = ', '.join(f"{color}={self.count[color]}" for color in self.count)
        return f"{type(self).__name__}({params})\n"


class Counter():
    def spread(**kwargs):
        spread_contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                spread_contents.append(key)
        return spread_contents
    # def count(spread):
    #     count = {}
    #    for item in spread:
    #        if item not in count:
    #            count[str(item)] = 1
    #        else:
    #            count[item] += 1
    #    return count


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__=='__main__':
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    print(str(hat1), '\n'+str(hat2), '\n'+str(hat3))
