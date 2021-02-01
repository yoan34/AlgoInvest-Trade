'''
Ce fichier lance l'algorithme 'brut' et 'optmiser' avec différents paramètre possible:
    -main.py brut -> lance l'algorithme brut
    -main.py optimiser money(int) -> lance l'algorithme optimiser sur le fichier CSV avec une money défini
    -main.py optimiser money(int) small -> lance l'agorithme optimiser sur le fichier CSV avec les 20 actions du brut
        et la money définit.
    -main.py optimiser money(int) new -> lance l'algorithme optimiser sur un nouveau jeu de 100.000 actions
        et la money définit.
    -main.py optimiser money(int) new len_data(int) -> lance l'algorithme optimiser sur un nouveau jeu de 'len_data' actions
        et la money définit.
'''
import os
import csv
import sys
import time

from data import shares, create_shares
from brut import brut
from optimiser import optimiser


def main():
    os.system('cls')
    os.system('clear')

    if len(sys.argv) == 1:
        print('Choose at least one argument (brut, optimiser).')
        return
    if sys.argv[1] == 'brut':
        brut(shares)

    elif sys.argv[1].upper() == 'H' or sys.argv[1].upper() == 'HELP':
        print("Ce fichier lance l'algorithme 'brut' et 'optmiser' avec différents paramètre possible:\n\n\
            -main.py brut -> lance l'algorithme brut\n\n\
            -main.py optimiser money(int) -> lance l'algorithme optimiser sur le fichier CSV avec une money défini\n\n\
            -main.py optimiser money(int) small -> lance l'agorithme optimiser sur le fichier CSV avec les 20 actions du brut\n\
                et la money définit.\n\n\
            -main.py optimiser money(int) new -> lance l'algorithme optimiser sur un nouveau jeu de 100.000 actions\n\
                et la money définit.\n\n\
            -main.py optimiser money(int) new len_data(int) -> lance l'algorithme optimiser sur un nouveau jeu de 'len_data' actions\n\
                et la money définit.\n\n\
            exemples:\n\
            main.py optimiser 499.4 new 250000\n\
            main.py brut\n\
            main.py optimiser 500\n\
            main.py optimiser 500 new")
        
    elif sys.argv[1] == 'optimiser':
        args = sys.argv[2:]
        if len(args) < 1:
            print('two arguments is required. (money)')
            return

        money = None
        format_data = 'csv'
        len_data = None
        min_cost = max_cost = min_profit = max_profit = None

        i = 0
        while args:
            if i == 0:
                try:
                    float(args[i])
                    if float(args[i]) < 1 or float(args[i]) > 1000000000:
                        print('Money (argument {}) must be between [1 - 1.000.000.000]'.format(i+3))
                        return
                    else:
                        money = float(args[i])
                except ValueError:
                    print('arguments in position {} must be a number'.format(i+3))
                    return
            elif i == 1:
                if args[i] == 'new' or args[i] == 'csv' or args[i] == 'small':
                    format_data = args[i]
                else:
                    print("Format data(argument {}) must be 'new', 'csv', or 'small'.".format(i+3))
                    return
            elif i == 2:
                if args[1] != 'new':
                    print('too many arguments.')
                    return
                else:
                    try:
                        int(args[i])
                        if int(args[i]) < 1000 or int(args[i]) > 10000000:
                            print('number of data (argument {}) must be between [1.000 - 10.000.000]'.format(i+3))
                            return
                        else:
                            len_data = int(args[i])
                    except ValueError:
                        print('arguments in position {} must be a number'.format(i+3))
                        return
            

            if i == len(args)-1:
                break
            i += 1
        
        if format_data == 'csv':
            data = []
            with open("dataFinance.csv") as file:
                csv_file = csv.reader(file)
                for i, line in enumerate(csv_file):
                    id, share, cost, profit = line
                    if i != 0:
                        data.append({
                            'id': id,
                            'share': share,
                            'cost': float(cost),
                            'profit': float(profit)
                            })
            optimiser(data, money, csv=True)
        elif format_data == 'small':
            optimiser(shares, money, small=True)

        else:
            args = list(filter(lambda x: x is not None,[len_data, min_cost, max_cost, min_profit, max_profit]))
            data = create_shares(*args)
            optimiser(data, money)

    else:
        print('first argument invalid Choose (brut, optimiser)')

if __name__ == '__main__':
    main()
