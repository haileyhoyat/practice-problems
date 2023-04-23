#https://edabit.com/challenge/xRMQG4Sxewx5agDRr

def find_highest(list):
    while len(list) > 1:
        if list[0] > list[1]: 
            highest = list[0]
            list.pop(1)
            find_highest(list)
        elif list[0] < list[1]:
            highest = list[1]
            list.pop(0)
            find_highest(list)
        elif list[0] == list[1]:
            highest = list[0]
            return highest
    else:
        highest = list[0]
        return highest


if __name__ == '__main__':
    list = [5,10,100,90,5]
    print(find_highest(list))

"""


"""
