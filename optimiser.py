import os
import csv

import time
from itertools import combinations
from functions import pgcd, get_number_with_2, is_divide, get_profit


def optimiser(data, money, csv=False, small=False):
    t1 = time.time()
    MONEY = money
    #------------------------------------
    #-------- start with xxx$ -----------
    #------------------------------------
    s1 = "OPTIMISER {}{} len data: {}".format('CSV' if csv else '', 'data create' if (not small and not csv) else '', len(data))
    print(s1.center(38))
    print(' '*5 + '-'*26)
    _start_money = " start with {}$ ".format(MONEY).center(26, '-')
    print("{}{}".format(' '*5, _start_money))
    print(' '*5 + '-'*26 + '\n')


    # Calcule et affiche le meilleur bénéfice possible selon les données en entrée
    a = time.time()
    best_benef = max([d['profit'] for d in data])
    b = time.time()
    print("{}TIME [ {:4}ms ]: find best benefit: {}%".format(' '*5,round(b-a,3)*10**3, best_benef))

    MAX_BENEFIT_POSSIBLE = MONEY*10* best_benef/1000

    # Calcule et affiche le temps pour trier les données par coût et profit.
    a = time.time()
    data = sorted(data, key=lambda x: (x['cost'], -x['profit']))
    b = time.time()
    print("{}TIME [ {:4}ms ]: sort by cost and profit.".format(' '*5,round(b-a,3)*10**3))

    actions, total_profit = [], 0

    # On calcule pour chaque action dans les données si son coût est un diviseur de l'argent total.
    # Si c'est un diviseur, on affiche le nombre d'achat nécessaire pour obtenir l'argent total,
    # sinon si l'action est potentiellement une des meilleurs actions, on la stock dans une liste
    # tant que la liste n'excède pas 50 actions.
    for d in data:
        if d['cost'] > MONEY:
            break
        
        # On regarde si il y a un diviseur direct si le profit est le MAXIMUM possible
        n = is_divide(MONEY*10, d['cost']*10) if d['profit'] == best_benef else False

        # Si un diviseur direct est trouvé, on affiche l'action et le nombre d'achat et on s'arrête ici.
        if n:
            print('\n{}purchases   {} X {}$ = {}$   with profit {}%\n'.format(' '*5, n, d['cost'],MONEY, d['profit']))
            total_profit += n *d['cost'] * d['profit']
            print('\n{}MAX IDEAL PROFIT: {}$'.format(' '*5, MAX_BENEFIT_POSSIBLE))
            print("{}TOTAL PROFIT: {}$\n".format(' '*5, round(total_profit/100, 3)))
            t2 = time.time()
            print("{}TOTAL TIME [ {}ms ]".format(' '*5, round(t2-t1,3)*10**3))
            break

        # on stock les meilleurs actions (profit = meilleur profit possible) si le jeu de données et
        # suffisament grand ( >= 10000 ). Sinon on stocks la meilleure action en terme de profit pour
        # différentes actions qui ont le même coût
        if len(data) >= 10000:
            if d['profit'] == best_benef and (not actions or actions[-1]['cost'] != d['cost']):
                actions.append(d)
        elif not actions or actions[-1]['cost'] != d['cost']:
            actions.append(d)

        # On estime de façon arbitraire que les 300 meilleurs actions suffisent à trouvé dans 99.999% des cas la meilleurs
        # combinaison de deux actions qui donne le meilleur profit.
        if len(actions) == 300:
            break


    # Si on a pas trouvé de diviseur direct de l'argent, alors on doit chercher une pair d'actions A et B ou
    # pgcd(A, B) = 1 et (A x B) - (A + B) + 1 <= argent
    if not n:
        actions = sorted(actions, key=lambda x: (-x['profit'], x['cost']))

        x = time.time()
        
        all_benef = []

        # On créer toutes les combinaisons possible des meilleurs actions par groupe de 2.
        combi_actions= list(combinations(actions, 2))

        for _actions in combi_actions:
            # On doit trié pour que la meilleurs action (meilleur profit) se trouvr en deuxième position.
            action1, action2 = sorted(_actions, key=lambda x: x['profit'])

            # Le pgcd nous permet d'éviter des scénarios ou un nombre N ne peut pas
            # se décomposer par deux nombre A et B ou (N / pgcd(A, B)) n'est pas un entier.

            if len(data) == 20: # on utilise le jeu de données de 20 actions
                if pgcd(action1['cost'], action2['cost']) == 1:
                    a,b = get_number_with_2(action1['cost'], action2['cost'], MONEY)
                else:
                    continue
            else:
                if (pgcd(action1['cost']*10, action2['cost']*10) == 1 and (action1['cost'] * action2['cost']
                    - (action1['cost'] + action2['cost']) + 1) <= MONEY):
                    a, b = get_number_with_2(action1['cost']*10, action2['cost']*10, MONEY*10)
                else:
                    continue

            all_benef.append({
                'profit': get_profit(a, action1, b, action2),
                'share1': {'n': a, 'cost': action1['cost'], 'profit': action1['profit'], 'name': action1['share']},
                'share2': {'n': b, 'cost': action2['cost'], 'profit': action2['profit'], 'name': action2['share']},
            })  
            # On peut augmenter la performance pour ne faire sortir qu'une possibilités
            # break

            
        y = time.time()
        print("{}TIME [ {:4}ms ]: get best possibilities of shares".format(' '*5,round(y-x,3)*10**3))

        # Si aucun couple n'est trouvé, alors on récupère la première actions stocké parmis les meilleurs
        if not all_benef:
            n = MONEY // actions[0]['cost']
            print('\n{}purchases   {} X {}$ = {}$   with profit {}%\n'.format(' '*5, n, actions[0]['cost'],
                n*actions[0]['cost'], actions[0]['profit']))
            total_profit += n *actions[0]['cost'] * actions[0]['profit']
            print('\n{}MAX IDEAL PROFIT: {}$'.format(' '*5, MAX_BENEFIT_POSSIBLE))
            print("{}TOTAL PROFIT: {}$".format(' '*5, round(total_profit/100, 3)))
            print('{}MONEY REMAINDER: {}$'.format(' '*5, ((MONEY*10-(n*actions[0]['cost']*10))/10)))
            return

        # On cherche et trouve le meilleur couple d'action qui donne le meilleur profit
        max_benef = max(all_benef, key=lambda x: x['profit'])['profit']

        # On filtre dans tous les couples d'actions qui à le même profit que le meilleur profit.
        all_max_benef = list(filter(lambda x: x['profit'] == max_benef, all_benef))
        t2 = time.time()

        if len(all_max_benef) > 50:
            print("\n{} 50 of the {} possibilities for a profit of {}$ ".format(' '*10, len(all_max_benef), max_benef))
        else:
            print("\n{} {} possibilities for a profit of {}$ ".format(' '*10, len(all_max_benef), max_benef))

        # On affiche les 50 premiers couple d'actions qui donne le meilleurs profit.
        for al in all_max_benef[:50]:
            print('{}purchases {:7} X {:7}$ ({}%)  +  {:7} X {:7}$ ({}%) = {}   ({} - {})'.format(' '*15, al['share1']['n'], al['share1']['cost'],
                al['share1']['profit'], al['share2']['n'], al['share2']['cost'], al['share2']['profit'], MONEY,
                al['share1']['name'], al['share2']['name']))


        print('\n{}MAX IDEAL PROFIT: {}$'.format(' '*5, MAX_BENEFIT_POSSIBLE))
        print("{}TOTAL PROFIT: {}$".format(' '*5, round(max_benef, 3)))
        print("\n{}TOTAL TIME [ {}ms ]".format(' '*5, round(t2-t1,3)*10**3))

        #------------------------------------
        #--------------- END ----------------
        #------------------------------------
        print('\n')
        print(' '*5 + '-'*26)
        _start_money = "END".format(MONEY).center(26, '-')
        print("{}{}".format(' '*5, _start_money))
        print(' '*5 + '-'*26 + '\n')


