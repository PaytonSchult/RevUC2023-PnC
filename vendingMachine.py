items = [
    {
        'code':0,
        'name':'Coca-Cola',
        'price': 1.50
    },
    {
        'code':1,
        'name':'Sprite',
        'price': 1.50
    },
    {
        'code':2,
        'name':'Dr. Pepper',
        'price': 1.50
    },
    {
     'code':3,
     'name':'Mountain Dew',
     'price': 1.50   
    },
    {
     'code':4,
     'name':'Fanta Orange',
     'price': 1.50
    },
    {
     'code':5,
     'name':'Fanta Grape',
     'price': 1.50
    },
    {
     'code':6,
     'name':'Monster',
     'price': 2.00
    },
    {
     'code':7,
     'name':'Red Bull',
     'price': 2.00   
    },
    {
     'code':8,
     'name':'WhiteClaw',
     'price': 3.00
    },
    {
     'code':9,
     'name':'Truly',
     'price': 3.00
    },
    {
     'code':10,
     'name':'Naturday',
     'price': 3.00
    },
    {
     'code':11,
     'name':'Corona',
     'price': 3.00   
    },
    {
     'code':12,
     'name':'Skittles',
     'price': 1.00   
    },
    {
     'code':13,
     'name':'M&Ms',
     'price': 1.00   
    },
    {
     'code':14,
     'name':'Sour Patch Kids',
     'price': 1.00   
    },
    {
     'code':15,
     'name':'Swedish Fish',
     'price': 1.00   
    },
    {
     'code':16,
     'name':'Hershey Bar',
     'price': 1.00   
    },
    {
     'code':17,
     'name':'3 Musketeers',
     'price': 1.00   
    },
    {
     'code':18,
     'name':'Snickers',
     'price': 1.00   
    },
    {
     'code':19,
     'name':'Lays Potato Chips',
     'price': 1.00   
    },
    {
     'code':20,
     'name':'Doritos',
     'price': 1.00   
    },
    {
     'code':12,
     'name':'Cool Ranch Doritos',
     'price': 1.00   
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dollars")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')