#!/usr/bin/env python3

from colorama import Fore
from colorama import Style
# https://pages.github.com/


def run(lis):
    length = len(lis)
    for i in range(length):
        print("i = " + str(i))
        print(lis)
        print("\n")

        for j in range(0, length-i-1):
            if len(lis[0:j]) > 0:
                print("[" + str(lis[0:j])[1:-1] + f', {Fore.LIGHTRED_EX}' + str(lis[j]) + f'{Style.RESET_ALL}, '
                                                                                    f'{Fore.LIGHTGREEN_EX}'
                      + str(lis[j+1]) + f'{Style.RESET_ALL}, ' + str(lis[j+2:length])[1:-1] + "]")
            else:
                print("[" + f'{Fore.LIGHTRED_EX}' + str(lis[j]) + f'{Style.RESET_ALL}, 'f'{Fore.LIGHTGREEN_EX}'
                      + str(lis[j + 1]) + f'{Style.RESET_ALL}, ' + str(lis[j + 2:length])[1:-1] + "]")

            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

                if len(lis[0:j]) > 0:
                    print("[" + str(lis[0:j])[1:-1] + f', {Fore.LIGHTGREEN_EX}' + str(lis[j+1]) +
                          f'{Style.RESET_ALL}, {Fore.LIGHTRED_EX}'
                          + str(lis[j]) + f'{Style.RESET_ALL}, ' + str(lis[j + 2:length])[1:-1] + "]")
                else:
                    print("[" + f'{Fore.LIGHTGREEN_EX}' + str(lis[j + 1]) +
                          f'{Style.RESET_ALL}, {Fore.LIGHTRED_EX}'
                          + str(lis[j]) + f'{Style.RESET_ALL}, ' + str(lis[j + 2:length])[1:-1] + "}")
            print("\n")
    return lis


list22323232 = [3, 4, 1, 5, 2, 0]
print(run(list22323232))
