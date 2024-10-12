import os
from time import sleep

# CONSTANTS

# TIME
SWAP_SLIDE_TIME = 3

# FOR FLAG
FLAG_LENGTH = 35
FLAG_WIDTH = 2
COLOR_ID = {'yellow': '\u001b[48;5;226m', 'green': '\u001b[48;5;28m', 'red': '\u001b[48;5;196m', 'default': '\u001b[0m'}
COLOR_ORDER = ('yellow', 'green', 'red')

# FOR PATTERN
SYMBOL_PAT = '\u001b[40m   \u001b[0m'
PATTERN_REPEAT_AMOUNT = 4

# FOR GRAPH Y=|X|
SYMBOL_GRAPH = '\u001b[48;5;231m   \u001b[0m'
HEIGHT_GRAPH = 9

# FOR CHART
SYMBOL_CHART1 = '\u001b[48;5;19m|\u001b[0m'
SYMBOL_CHART2 = '\u001b[48;5;124m|\u001b[0m'
SCALE = 100
FILENAME = 'sequence.txt'


def draw_lithuania_flag():
    for i in range(len(COLOR_ORDER)):
        for j in range(FLAG_WIDTH):
            print(COLOR_ID[COLOR_ORDER[i]] + ' ' * FLAG_LENGTH + COLOR_ID['default'])


def draw_pattern_e(amount=PATTERN_REPEAT_AMOUNT):
    for i in range(amount):
        print("/\\    " * amount)
        print("  \\/  " * amount)


def draw_graph_modx():
    for i in range(HEIGHT_GRAPH, -1, -1):
        spaces = " " * i
        stars = "*" * (HEIGHT_GRAPH - i)
        print(spaces + "*" + stars)


def draw_chart():
    even = 0
    odd = 0
    with open(FILENAME) as f:
        check = True
        for num in [abs(float(el.rstrip())) for el in f.readlines()]:
            if check:
                odd += num
            else:
                even += num
            check = not check
        percent_even_cages = round(SCALE * (even / (odd + even)))
        percent_odd_cages = round(SCALE * (odd / (odd + even)))
        fill_chart(title='EVENS', percent_cages=percent_even_cages, abs_sum=round(even, 2), symbol_type=SYMBOL_CHART1)
        fill_chart(title='ODDS', percent_cages=percent_odd_cages, abs_sum=round(odd, 2), symbol_type=SYMBOL_CHART2)
        print(f'\nTotal: {round(odd + even, 2)}')


def fill_chart(title, percent_cages, abs_sum, symbol_type):
    print(title)
    for i in range(SCALE):
        if percent_cages != 0:
            percent_cages -= 1
            print(symbol_type, end='')
        else:
            print('|', end='')
    print(f'\tABS SUM: {abs_sum}')


def main():
    funcs = [draw_lithuania_flag, draw_pattern_e, draw_graph_modx, draw_chart]
    i = 0
    while True:
        funcs[i]()  
        i = (i + 1) % len(funcs)  
        sleep(SWAP_SLIDE_TIME)  
        os.system("cls" if os.name == "nt" else "clear")  


if name == 'main':
    main()
    
