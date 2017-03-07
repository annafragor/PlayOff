import random
import math
import sys


def game(cmd1, cmd2):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    while (num2 == num1):
        num2 = random.randint(0, 10)

    if (num1 > num2):
        return [cmd1, str(num1) + ":" + str(num2)]
    else:
        return [cmd2, str(num2) + ":" + str(num1)]


def game_round(shuf_cmds):
    '''заполняется один уровень для 1/n-финала и удаляются проигравшие команды'''
    level = {}
    n = len(shuf_cmds)
    i = 0
    while (i < n):
        winner = game(shuf_cmds[i], shuf_cmds[i + 1])

        if (winner[0] == shuf_cmds[i + 1]):
            shuf_cmds[i], shuf_cmds[i + 1] = shuf_cmds[i + 1], shuf_cmds[i]

        level[shuf_cmds[i]] = [shuf_cmds[i + 1], "won", winner[1]]
        level[shuf_cmds[i + 1]] = [shuf_cmds[i], "lost", winner[1][::-1]]
        shuf_cmds.remove(shuf_cmds[i + 1])
        n -= 1
        i += 1  # i -= 1; i += 2

    return level


def emulate_playoff():
    print("input the names of your commands")
    commands = []
    command = input()
    while (command != ""):
        if (command not in commands):
            commands.append(command)
        command = input()
    all_commands = commands[:]

    log2_commands = math.log2(len(commands))
    if log2_commands % 1 != 0:
        print("number of commands isn't 2^n, so the program stops now.")
        sys.exit()

    playoff = []
    for i in range(int(log2_commands)):
        random.shuffle(commands)
        level = game_round(commands)
        playoff.append(level)

    playoff.append(commands[0])
    playoff.append(all_commands)
    return playoff
