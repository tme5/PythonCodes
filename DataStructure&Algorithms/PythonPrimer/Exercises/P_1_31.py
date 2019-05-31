#!python
'''
Created on Apr 5, 2019

@author: TME5
'''
# +---{ Import Section }---+
import sys,os,time
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

balance=0

def getNotes(notes_list):
    global balance
    ret_n=0
    min_n=min(notes_list)
    for n in notes_list:
        if n == balance:
            return [n]
            balance=balance-n
        if n < balance:
            ret_n=n
    balance=balance-ret_n
    if balance>=min_n:
        return [ret_n]+getNotes(notes_list)
    else:
        return [ret_n]
    
def getCoins(coins_list):
    global balance
    ret_c=0
    min_c=min(coins_list)
    for c in coins_list:
        if c == balance:
            balance=balance-c
            return [c]
        if c < balance:
            ret_c=c 
    balance=balance-ret_c
    if balance>=min_c:
        return [ret_c]+getCoins(coins_list)
    else:
        return [ret_c]

def getChange():
    global balance
    coins_list=[1,2,5]
    notes_list=[10,20,100,500,2000]
    ret_notes=getNotes(notes_list)
    ret_coins=getCoins(coins_list)
    return ret_notes,ret_coins,balance

    
def makeChange(amount_charged,amount_given):
    global balance
    balance=amount_given-amount_charged
    if balance < 0:
        print('Amount given is less than charged')
        return
    else:
        ret=getChange()
        return ret
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    amount_charged=1990.5
    amount_given=2000
    Notes,coins,balance=makeChange(amount_charged,amount_given)
    print('--- Return Notes ---')
    for note in Notes:
        if note > 0:
            print(note)
    print('--- Return Coins ---')
    for coin in coins:
        if coin > 0:
            print(coin)
    
    print(f'--- Can\'t return balance {balance}')
            
    
    
if __name__ == '__main__': main()