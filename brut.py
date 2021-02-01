import time
from functions import get_number_with_5
from itertools import permutations

def brut(shares):
    
    BASE_MONEY = 500
    MAX_BENEFIT_POSSIBLE = 500*0.27
    print('BRUT'.center(36))
    print(' '*5 + '-'*26)
    _start_money = " start with {}$ ".format(BASE_MONEY).center(26, '-')
    print("{}{}".format(' '*5, _start_money))
    print(' '*5 + '-'*26 + '\n')

    t1 = time.time()
    # On crée toutes les permutations possibles pour des couples de 5 actions dans 20 actions.
    shares = list(permutations(shares, 5))
    t2 = time.time()
    print("{}TIME [ {:4}ms ]: create all permutations by 5.".format(' '*5,round(t2-t1,3)*10**3))

    arr = []

    t1 = time.time()

    # Pour chaque couple de 5 actions, on les trie par ordre de profit croissant, puis on test
    # si les 5 actions peuvent obtenir l'argent investis.
    for i,share in enumerate(shares):
        if i % 100 == 0:
            print("{}{:.2f}%\r".format(' '*5,i * (100/len(shares))), end='', flush=True)
        new_share = sorted(share, key=lambda x: x['profit'])

        # On test si les 5 actions peuvent composer exactement l'argent investis.
        a,b,c,d,e = get_number_with_5(new_share[0]['cost'],new_share[1]['cost'],
            new_share[2]['cost'],new_share[3]['cost'], new_share[4]['cost'], BASE_MONEY)

        # Si les 5 actions peuvent composer l'argent investis, on calcule le profit et on
        # le stock dans une liste (arr).
        if a != -1:
            profit = (
                (a*new_share[0]['cost']*new_share[0]['profit'] +
                b*new_share[1]['cost']*new_share[1]['profit'] +
                c*new_share[2]['cost']*new_share[2]['profit'] +
                d*new_share[3]['cost']*new_share[3]['profit'] +
                e*new_share[4]['cost']*new_share[4]['profit'])/100
            )
            arr.append({
                'profit': profit,
                'share1': (a, new_share[0]),
                'share2': (b, new_share[1]),
                'share3': (c, new_share[2]),
                'share4': (d, new_share[3]),
                'share5': (e, new_share[4]),
            })

    t2 = time.time()
    print("{}TIME [ {:4}ms ]: find all profit of permutations".format(' '*5,round(t2-t1,3)*10**3))

    t1 = time.time()

    # On récupère parmis toutes les combinaisons de couple de 5 actions qui peuvent composer l'argent
    # investis celle qui à le meilleur profit et on l'affiche.
    best = max(arr, key=lambda x: x['profit'])
    print('\n{}purchases {} X {}$ ({}%) + {} X  {}$ ({}%) + {} X {}$ ({}%) + {} X {}$ ({}%) + {} X {}$ ({}%) = {}$\n'.format(
        ' '*5,
        best['share1'][0], best['share1'][1]['cost'], best['share1'][1]['profit'],
        best['share2'][0], best['share2'][1]['cost'], best['share2'][1]['profit'],
        best['share3'][0], best['share3'][1]['cost'], best['share3'][1]['profit'],
        best['share4'][0], best['share4'][1]['cost'], best['share4'][1]['profit'],
        best['share5'][0], best['share5'][1]['cost'], best['share5'][1]['profit'],
        BASE_MONEY
    ))
    t2 = time.time()
    print("{}TIME [ {:4}ms ]: find best profit".format(' '*5,round(t2-t1,3)*10**3))

    print('\n{}MAX IDEAL PROFIT: {}$'.format(' '*5, MAX_BENEFIT_POSSIBLE))
    print("{}TOTAL PROFIT: {}$".format(' '*5, round(best['profit'], 3)))

    #------------------------------------
    #--------------- END ----------------
    #------------------------------------
    print('\n')
    print(' '*5 + '-'*26)
    _start_money = "END".format(BASE_MONEY).center(26, '-')
    print("{}{}".format(' '*5, _start_money))
    print(' '*5 + '-'*26 + '\n')


