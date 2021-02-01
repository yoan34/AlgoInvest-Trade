import random

shares = [
    {'share': 'share-1', 'cost': 15, 'profit': 10},
    {'share': 'share-2', 'cost': 25, 'profit': 15},
    {'share': 'share-3', 'cost': 35, 'profit': 20},
    {'share': 'share-4', 'cost': 30, 'profit': 17},
    {'share': 'share-5', 'cost': 40, 'profit': 25},
    {'share': 'share-6', 'cost': 11, 'profit': 7},
    {'share': 'share-7', 'cost': 13, 'profit': 11},
    {'share': 'share-8', 'cost': 24, 'profit': 13},
    {'share': 'share-9', 'cost': 17, 'profit': 27},
    {'share': 'share-10', 'cost': 21, 'profit': 17},
    {'share': 'share-11', 'cost': 55, 'profit': 9},
    {'share': 'share-12', 'cost': 19, 'profit': 23},
    {'share': 'share-13', 'cost': 7, 'profit': 1},
    {'share': 'share-14', 'cost': 9, 'profit': 3},
    {'share': 'share-15', 'cost': 4, 'profit': 8},
    {'share': 'share-16', 'cost': 2, 'profit': 12},
    {'share': 'share-17', 'cost': 5, 'profit': 14},
    {'share': 'share-18', 'cost': 12, 'profit': 21},
    {'share': 'share-19', 'cost': 57, 'profit': 18},
    {'share': 'share-20', 'cost': 10, 'profit': 5},
]

def create_shares(n=100000, min_cost=100, max_cost=1000, min_profit=1, max_profit=19):
    data = []
    for i in range(n):
        if min_cost > max_cost:
            print('minimum of cost must be less than the maximumm of cost.')
            return
        if min_profit > max_profit:
            print('minimum of profit must be less than the maximum of profit.')
            return
        cost = random.randint(min_cost, max_cost)/10
        profit = float(random.randint(min_profit, max_profit))
        share ='share-{}'.format(i)
        id = i
        data.append({'id': id, 'share': share, 'cost': cost, 'profit': profit})
    return data
