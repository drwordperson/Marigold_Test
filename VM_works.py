# What does a vending machine do?

# Greets you with the nature of your existence and informs you of available transactions

# Accepts coins

# You push buttons

# It dispenses beverage

# You take beverage

# Apply remaining coins to a future transaction?

# End transaction

print('Welcome to the Wonderful-World-of-Friz-Kola vending machine!')

print('This machine only takes US quarters, and one beverage costs $0.50.')

coins_n = input('How many coins do you put in?')

coins_i = int(coins_n)

if coins_i < 0:
    raise ValueError('Negative values not allowed!  You may not rob the vending machine in this fashion!')
    quit()
else:
    pass
    
while coins_i < 2:
    credit = coins_i*.25
    print('Your current credit is:')
    print(credit)
    yn = input('You need at least $0.50 to purchase a beverage.  Do you wish to add more coins? y/n')
    if(yn == 'y'):
        coins_n = input('How many coins do you put in?')
        coins_j = int(coins_n)
        coins_i = coins_i + coins_j
        pass
    if(yn == 'n'):
        print('Sorry to see you go.  Have a good day!')
        print('The coin return gives you this many quarters:')
        print(coins_i)
        quit()
    else:
        print('Sorry, I needed the answer of either y or n.')
        print('The coin return gives you this many quarters:')
        print(coins_i)
        quit()

if coins_i >= 2:
    pass

    yn = input('Do you wish to purchase a beverage? y/n')
    if(yn == 'y'):
        print('Thank you for your purchase!  Share and enjoy.')
        print('The machine dispenses one beverage.')
        print('The coin return gives you this many quarters:')
        print(coins_i-2)
        quit()
    if(yn == 'n'):
        print('Sorry to see you go.  Have a good day!')
        print('The coin return gives you this many quarters:')
        print(coins_i)
        quit()
    if(yn == 'I HATE COLA!!!'):
        print('You punch the vending machine.  It falls over and crushes you like a bug.')
        print('The coin return gives you this many quarters:')
        print(coins_i*9987)
        print('Meanwhile, at the Pearly Gates, you lament your fate to St. Peter.')
        print('From his bored nodding, you can tell he has heard this one before.')
        quit()
    else:
        print('Sorry, I needed the answer of either y or n.')
        print('The coin return gives you this many quarters:')
        print(coins_i)
        quit()
    


            
#print('This machine serves three flavors of Fanta:  lemon, orange, and grape.')

#flavor = input('Which flavor do you choose?')

#print('You have no credit remaining.  Thank you for your business.  Share and enjoy!')

#yn = input('You have X credit remaining.  Do you wish to continue with another transaction?')







