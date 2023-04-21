#https://edabit.com/challenge/xRMQG4Sxewx5agDRr

def find_highest(list):
    
    if list[0] > list[1]: 
        highest = list[0]
        list.pop(1)
    elif list[0] < list[1]:
        highest = list[1]
        list.pop(0)
    else:
        print(highest)
        return

    if len(list) > 1:
        find_highest(list)
    else:
        print(highest)


if __name__ == '__main__':
    list = [5,1001,1001,89]
    find_highest(list)

"""


"""