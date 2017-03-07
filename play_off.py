#! /usr/bin/env python
import emulation

results = emulation.emulate_playoff()
all_teams = results.pop()
winner = results.pop()
print("winner - " + winner)

client_cmd = ""
while (client_cmd != "exit"):
    print("If you want to get info about definite team, input its name. \nIf you want to exit - input 'exit'")
    client_cmd = input()

    if (client_cmd not in all_teams) and (client_cmd != "exit"):
        print("there wasn't such a team in the championship.")
        continue

    '''if we want info about certain team:'''
    i = 0
    while (i < len(results)):
        if (client_cmd in results[i]):
            if (i < len(results) - 1):
                print("In 1/", len(results[i]) // 2, "-", sep='', end='')
            else:
                print("In ", end='')

            print("final", client_cmd, results[i][client_cmd][1],
                  results[i][client_cmd][0], "with score", results[i][client_cmd][2])
            i += 1
        else:
            break
