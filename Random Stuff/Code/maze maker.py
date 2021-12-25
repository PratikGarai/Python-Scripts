#!/usr/bin/python3
import random
def _get_next_step():
    prob_list = [1, 2, 2]
    next_step_choices = [[0, -1], [ 1, 0], [ 0, 1]]
    return random.choices(next_step_choices, weights = prob_list)[0]

def make_maze(n):
    initial_template = [[0 for _ in range(n)] for _ in range(n)]
    maze = initial_template
    intersect_choices=[]

    x, y = 0, 0
    while (x < n and y < n):
        maze[x][y] = 1
        next_step = _get_next_step()
        x += next_step[0]
        y += next_step[1] if y + next_step[1] > 0 else 1
        intersect_choices.append([x,y])
    intersect = [random.choice(intersect_choices)]

    x, y = n-1, n-1
    while (x > -1 and y > -1):
        maze[x][y] = 1
        next_step = _get_next_step()
        x -= next_step[0] if x - next_step[0] < n else 0
        y -= next_step[1] if y - next_step[1] < n else 0
        if x == intersect[0][0]:
            intersect.append([x,y])

    for i in range(intersect[0][1],intersect[1][1]):
        maze[intersect[0][0]][i]=1

    for i in range(50):
        random.choice(maze)[random.randint(0,15)] = 1
    
    return maze

if __name__ == '__main__':
    print('Enter length')
    n = int(input())
    l = make_maze(n)
    for i in range(n):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
  
