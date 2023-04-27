#https://edabit.com/challenge/towwrEJ7zr8xKGSr5



def robot_path(directions):

    destination1 = [3,2]
    destination2 = [-4, 3]
    robot = [0,0]

    for i in directions:
        if i == "n":
            robot[1] = robot[1] + 1
        elif i == "e":
            robot[0] = robot[0] + 1
        elif i == "s":
            robot[1] = robot[1] - 1
        elif i == "w":
            robot[0] = robot[0] - 1

    if ((robot[0] == destination2[0]) and (robot[1] == destination2[1])) or ((robot[0] == destination1[0]) and (robot[1] == destination1[1])):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    robot1 = ["s", "e", "e", "n", "n", "e", "n"]
    robot2 = ["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]
    robot3 = ["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]
    
    robot_path(robot1)
    robot_path(robot2)
    robot_path(robot3)
    
    