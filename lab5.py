# Clayton Clark 92141310 and Terry Ng 73412738 Lab Section 11 Asst. 5

print()
print('-----------Part c.1--------------')
print()

# Part c.1

from collections import namedtuple

Dish = namedtuple('Dish', 'name price calories')
d1 = Dish('Pizza', 10, 400)
d2 = Dish('Bread', 5, 100)
d3 = Dish('Pizza', 14, 400)

print()
print('-----------Part c.2--------------')
print()

# Part c.2

def Dish_str(d:Dish) -> str:
    ''' Returns a string with the Dish in this form:
    Paht Woon Sen ($9.50): 330 cal '''
    x = d.name + ' ($' + str(d.price) + '): ' + str(d.calories) + ' cal'
    return x

print(Dish_str(d1))


print()
print('-----------Part c.3--------------')
print()

# Part c.3

def Dish_same(x: Dish, y: Dish) -> bool:
    '''Returns True if the names of the 2 dishes and their calorie counts
    are equal '''

    if x.name == y.name and x.calories == y.calories:
        return True
    else:
        return False
    
assert Dish_same(d1, d2) == False
assert Dish_same(d1, d3) == True

print()
print('-----------Part c.4--------------')
print()

# Part c.4

def Dish_change_price(d: Dish, x: int) -> Dish:
    '''Returns a Dish that's the same as the parameter except that its
    price is changed: a positive or negative number representing percentage
    change in price'''
    if x > 0:
        d = d._replace(price = d.price + d.price * x/100)
        return d
    else:
        d = d._replace(price = d.price + d.price * x/100)
        return d
assert Dish_change_price(d1, 100) == Dish('Pizza', 20, 400)
assert Dish_change_price(d1, -50) == Dish('Pizza', 5, 400)
assert Dish_change_price(d2, 50) == Dish('Bread', 7.5, 100)
assert Dish_change_price(d2, -10) == Dish('Bread', 4.5, 100)
assert Dish_change_price(d3, 80) == Dish('Pizza', 25.2, 400)
assert Dish_change_price(d3, -60) == Dish('Pizza', 5.6, 400)

print()
print('-----------Part c.5--------------')
print()

# Part c.5

def Dish_is_cheap(d: Dish, x:int) -> bool:
    '''Returns True if the Dish's price is less than x'''
    if d.price < x:
        return True
    else:
        return False
assert Dish_is_cheap(d1, 20) == True
assert Dish_is_cheap(d1, 5) == False

print()
print('-----------Part c.6--------------')
print()

# Part c.6

DL = [Dish('Pizza', 10, 400),
Dish('Bread', 5, 100),
Dish('Lasagna', 14, 400),
Dish('Pasta', 12, 250),
Dish('Burger', 8, 500)]

DL2 = [Dish('Sandwich', 20, 270),
Dish('Fish', 12, 200),
Dish('Eggroll', 50, 250),
Dish('Curry', 40, 300)]

DL.extend(DL2)
print(DL)

def Dishlist_display(L: list) -> str:
    '''Returns one large string consisting of the string representation
    of each dish followed by a newline'''
    for x in range(len(L)):
        print(L[x])


print()
print('-----------Part c.7--------------')
print()

# Part c.7

def Dishlist_all_cheap(d: list, x: int) -> bool:
    '''Returns True if the price of every dish on the list is less than
    the number'''
    for i in d:
        if Dish_is_cheap(i, x) == True:
            return True
        else:
            return False

assert Dishlist_all_cheap(DL, 100) == True
assert Dishlist_all_cheap(DL, 5) == False

print()
print('-----------Part c.8--------------')
print()

# Part c.8

def Dishlist_change_price(L: list, x: float) -> list:
    '''Returns a list of Dishes with each price changed by the specified amount
    '''
    y = []
    for i in L:
        y.append(Dish_change_price(i, x))
    return y
        
print(Dishlist_change_price(DL, 10.0))

print()
print('-----------Part c.9--------------')
print()

# Part c.9

def Dishlist_prices(L: list) -> list:
    '''Takes a list of Dishes and returns a list of numbers containing
    just the prices of the dishes on the list'''
    result = []
    for p in L:
        result.append(p.price)
    return result
print(Dishlist_prices(DL))

print()
print('-----------Part c.10--------------')
print()

# Part c.10

def Dishlist_average(L: list) -> float:
    '''Takes a list of Dishes and returns the average price of those dishes'''
    sum = 0
    for a in Dishlist_prices(L):
        sum += a
    return sum/len(L)
    
print(Dishlist_average(DL))

print()
print('-----------Part c.11--------------')
print()

# Part c.11

def Dishlist_keep_cheap(L: list, x: int) -> list:
    ''' Takes a list of Dishes and a number and returns a list of those dishes
    on the original list that have prices less than the number'''
    result = []
    for k in L:
        if Dish_is_cheap(k, x) == True:
            result.append(k)
    return result

print(Dishlist_keep_cheap(DL, 10))
print(Dishlist_keep_cheap(DL, 30))

print()
print('-----------Part c.12--------------')
print()

# Part c.12

DL3 = [Dish('Pizza', 10, 400),
Dish('Bread', 5, 100),
Dish('Lasagna', 14, 400),
Dish('Pasta', 12, 250),
Dish('Burger', 12, 450),
Dish('Chicken', 30, 500),
Dish('Fish', 9, 200),
Dish('Tacos', 4, 200),
Dish('Spaghetti', 8, 350),
Dish('Burritos', 12, 600),
Dish('Bagel', 3, 100),
Dish('Cereal', 1, 100),
Dish('Eggs', 1, 150),
Dish('Toast', 2, 50),
Dish('Steak', 35, 700),
Dish('Shrimp', 15, 550),
Dish('Scallop', 20, 300),
Dish('Clams', 18, 200),
Dish('Oyster', 29, 250),
Dish('Salmon', 34, 300),
Dish('Corn', 7, 100),
Dish('Potatoes', 9, 300),
Dish('Peas', 4, 200),
Dish('Lettuce', 6, 100),
Dish('Cabbage', 6, 150)]

def before_and_after():
    price = int(input("Enter a number:" ))
    price
    Dishlist_display(DL3)
    print()
    for o in range(len(DL3)):
        DL3[o] = Dish_change_price(DL3[o], price)
    return Dishlist_display(DL3)

before_and_after()

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

print()
print('-----------Part e.1--------------')
print()

# Part e.1
r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('escargots', 12.95, 250),
                                                     Dish('poached salmon', 18.50, 550),
                                                     Dish('rack of lamb', 24.00, 850),
                                                     Dish('marjolaine cake', 8.50, 950)])

print(r3)

print()
print('-----------Part e.2--------------')
print()
# Part e.2

test = Restaurant('Pascal', 'French', '940-752-0107', [])

def Restaurant_first_dish_name(r: Restaurant) -> str:
    """takes a Restaurant as its argument and returns the name
    of the first dish on the restaurant's menu"""
    if r.menu == []:
        return ""
    else:
        return r.menu[0].name
        
        
    
assert(Restaurant_first_dish_name(r3)) == 'escargots'
assert(Restaurant_first_dish_name(test)) == ''



print()
print('-----------Part e.3--------------')
print()

# Part e.3

def Restaurant_is_cheap(r: Restaurant, x: int) -> bool:
    """takes two arguments, a Restaurant and a number, and returns True if
    the average price of the Restaurant's menu is less than or equal to
    the number"""
    if Dishlist_average(r.menu) <= x:
        return True
    else:
        return False
assert(Restaurant_is_cheap(r3, 10)) == False
assert(Restaurant_is_cheap(r3, 16)) == True

print()
print('-----------Part e.4--------------')
print()

# Part e.4
RL = [r1, r2, r3]

def Dish_raise_price(d: Dish) -> Dish:
    """Takes a Dish, changes the price of the Dish and returns it"""
    d = d._replace(price = d.price + 2.50)
    return d
    
assert(Dish_raise_price(d1)) == Dish(name='Pizza', price=12.5, calories=400)
assert(Dish_raise_price(d2)) == Dish(name= 'Bread', price=7.5, calories=100)

def Menu_raise_prices(m: Restaurant.menu) -> Restaurant.menu:
    """takes a Menu, applies a function like
    Dish_raise_price to each Dish on the Menu, and returns the modified menu."""
    for i in range(len(m)):
        m[i] = Dish_raise_price(m[i])
    return m
print("Menu_raise_prices")
print()
print(Menu_raise_prices(r3.menu))
print()
print()

def Restaurant_raise_prices(r: Restaurant) -> Restaurant:
    """takes a restaurant and returns that restaurant with
    all its prices raised by $2.50"""
    Menu_raise_prices(r.menu)
    return r
print("Restaurant_raise_prices")
print()
print(Restaurant_raise_prices(r2))
print()
print()


def Collection_raise_prices(C: 'list of Restaurant') -> 'list of Restaurant':
    """ takes a Collection and returns the Collection with the
    price of every dish at every restaurant raised by $2.50"""
    for x in C:
        Restaurant_raise_prices(x)
    return C
print("Collection_raise_prices")
print()
print(Collection_raise_prices(RL))
print()
print()
############################################ change by percent


def Dish_raise_percent(d: Dish, x: float) -> Dish:
    """Takes a Dish and a percent, changes the price of the Dish
    by a percent and returns it"""
    d = d._replace(price = d.price + d.price * x/100)
    return d
    
assert(Dish_raise_percent(d1, 100)) == Dish(name='Pizza', price=20, calories=400)
assert(Dish_raise_percent(d2, 100)) == Dish(name= 'Bread', price=10, calories=100)

def Menu_raise_percent(m: Restaurant.menu, x: float) -> Restaurant.menu:
    """takes a Menu and a percent, applies a function like
    Dish_raise_percent to each Dish on the Menu, and returns the modified menu."""
    for i in range(len(m)):
        m[i] = Dish_raise_percent(m[i],x)
    return m
print()
print("Menu_raise_percent")
print()
print(Menu_raise_percent(r3.menu, 100))
print()
print()
def Restaurant_raise_percent(r: Restaurant, x: float) -> Restaurant:
    """takes a restaurant and a percent returns that restaurant with
    all its prices raised by that percent"""
    Menu_raise_percent(r.menu, x)
    return r
print("Restaurant_raise_percent")
print()
print(Restaurant_raise_percent(r2, 100))
print()
print()

def Collection_change_price(C: 'list of Restaurant', x: float) -> 'list of Restaurant':
    """takes a Collection and a second parameter, a percentage by which to
    change each price and returns the Collection"""
    for i in C:
        Restaurant_raise_percent(i, x)
    return C
print("Collection_change_price")
print()
print(Collection_change_price(RL, 10.0))
print()


    
print()
print('-----------Part e.5--------------')
print()
# Part e.5

Restaurant_Collection = [r1, r2, r3]

def Collection_select_cheap(D: Dish, n: float)-> list:
    """takes a Collection and a number and returns a list of all the Restaurants
    in the collection whose average price is less than or equal to that number"""
    result = []
    for i in D:
        if Dishlist_average(i.menu) <= n:
            result.append(i)
    return result

print(Collection_select_cheap(Restaurant_Collection, 1000))
print()
print()
print(Collection_select_cheap(Restaurant_Collection, 30))

# For Parts e-4 and e-5, the functions change the restaurants( r1, r2, r3) in
# place and we did not make a new list to put the list of the modified
# restaurant in. So the functions change the price from the original prices
# then changes the price again after the next function that changes its new price
# and it repeats itself. So if the raise price function was used and the
# original price was $12, after the first function, it
# would be $14.50, and after the next function that changes it, it would be
# $17. The percent definitions also does the same starting from the changed
# prices of raise price by 2.50. We did this after lab so we were unsure
# whether to make new lists to store the modified prices of the restaurants.

print()
print('-----------Part g--------------')
print()

# Part g


Count = namedtuple('Count', 'letter number')

def letter_count_one(s1: str, s2: str)->Count:
    '''Counts each individual letter'''
    count = 0
    for x in s1:
        if x in s2:
            count +=1
    return Count(s2, count)

def letter_count(s1: str, s2:str)->Count:
    results = []
    for i in s2:
        results.append(letter_count_one(s1, i))
    return results


print(letter_count('The cabbage has baggage', 'abcd'))





        
    


    
    
                
                






    
    















    
    
    



        
