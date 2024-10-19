price = 0.75

def main():
    while True:
        print ('Accepted coins: 50p, 20p, 10p, 5p.')
        if update_price() == False:
            continue
        else:
            break

def remove_digits(input):
    return ''.join(char for char in input if char.isdigit())

def check_coin(coin):
    accepted_coins = ['50p','10p','20p','50p']
    if coin in accepted_coins:
        coin_raw = remove_digits(coin)
        coin_value = (0.01*float(coin_raw))
        return coin_value
    else:
        print ('Please insert accepted coin. Accepted coins are:', end=' ')
        for _ in accepted_coins:
            print (_,end=' ')
        return None

def get_coin():
    while True:
        coin = input('\nEnter a coin >')
        if check_coin(coin) != None:
            return check_coin(coin)
        else:
            continue

def update_price():
    global price
    coin = get_coin()
    price -= coin
    if price > 0:
        print (f'Paid £{coin}')
        print (f'Remaining to pay: £{price}')
        return False
    elif price <= 0:
        change = price*-1
        print (f"Here's your coffee. Change: {change}")
        return True

main()