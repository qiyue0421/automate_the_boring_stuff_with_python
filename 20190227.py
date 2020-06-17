"""
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}


def printBoard(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('--+--+--')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])


# printBoard(theBoard)
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Trun for ' + turn + '.Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
"""
Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(Inventory):
    print('Inventory:')
    total = 0
    for k, v in Inventory.items():
        print(k + ' ' + str(v))
    print('Total Inventory are: ' + str(total))


def add(Inventory, addItems):
    for i in range(len(addItems)):
        Inventory[addItems[i]] = Inventory.get(addItems[i], 0) + 1
    return Inventory



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add(inv, dragonLoot)
print(inv)
displayInventory(inv)
