import csv, random, sys
from tabulate import tabulate


def main():
    resetboard()
    while True:
        userdecision()
        endcondition()
        testdraw()
        botdecision()
        showboard()
        endcondition()


def testdraw():
    line = []
    with open('board.csv','r') as file:
        reader = csv.reader(file)
        for _ in reader:
            line.extend(_)
        if '.' in line:
            pass
        else:
            showboard()
            sys.exit('It is a draw!')

def endcondition():
    grid = []
    with open('board.csv','r') as file:
        reader = csv.reader(file)
        for _ in reader:
            grid.append(_)
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] == 'X' or grid[i][0] == grid[i][1] == grid[i][2] == 'O':
                showboard()
                sys.exit('Game over!')
            elif grid[0][i] == grid[1][i] == grid[2][i] == 'X' or grid[0][i] == grid[1][i] == grid[2][i] == 'O':
                showboard()
                sys.exit('Game over!')
            elif grid[0][0] == grid[1][1] == grid[2][2] == 'X' or grid[0][0] == grid[1][1] == grid[2][2] == 'O':
                showboard()
                sys.exit('Game over')
            elif grid[0][2] == grid[1][1] == grid[2][0] == 'X' or grid[0][2] == grid[1][1] == grid[2][0] == 'O':
                showboard()
                sys.exit('Game over')
            else:
                continue


def botdecision():  
    while True:
        grid = []
        a = random.randint(0,2)
        b = random.randint(0,2)
        with open('board.csv','r') as file:
            reader = csv.reader(file)
            for _ in reader:
                grid.append(_)
        grid = grid[::-1]
        if grid[a][b] == 'X' or grid[a][b] == 'O':
            continue
        else:
            grid[a][b] = 'O'
            break
    with open('board.csv','w') as file:
        writer = csv.writer(file)
        writer.writerows(grid[::-1])

def userdecision():
    while True:
        grid = []
        inp = input('Please input the coordinates of your X\n')
        with open('board.csv','r') as file:
            reader = csv.reader(file)
            for _ in reader:
                grid.append(_)
        grid = grid[::-1]
        if grid[int(inp.split(',')[-1])][int(inp.split(',')[-2])] == 'X' or grid[int(inp.split(',')[-1])][int(inp.split(',')[-2])] == 'O':
            continue
        else:
            grid[int(inp.split(',')[-1])][int(inp.split(',')[-2])] = 'X'
            break
    with open('board.csv','w') as file:
        writer = csv.writer(file)
        writer.writerows(grid[::-1])

def showboard():
    print(f'\n')
    with open('board.csv','r') as file:
        reader = csv.reader(file)
        print(tabulate(reader, tablefmt="grid"), end = f'\n\n')

def resetboard():
    with open('board.csv','w') as file:
        writer = csv.writer(file)
        for _ in range(3):
            writer.writerow(['.', '.', '.'])

if __name__ == '__main__':
    main()
