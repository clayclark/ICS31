#     Clayton Clark 92141310. ICS 31 Lab sec 11.


# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)
from collections import namedtuple

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 f:  Search the collection for selected cuisine
 d:  Search the collection for the selected dish
 p:  Print all the restaurants
 c:  Change prices for the dishes served

 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            n =float(input('Please enter percent: '))
            Collection_change_prices(C, n)
        elif response=='f':
            Collection_search_by_cuisine(C)
        elif response=='d':
            Collection_search_by_dish(C)

        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")

#### DISHES
Dish = namedtuple('Dish', 'name price calories')

def Dish_str(d: Dish) -> str:
    ''' Returns a string with the Dish in this form:
    Paht Woon Sen ($9.50): 330 cal '''
    x = d.name + ' ($' + str(d.price) + '): ' + str(d.calories) + ' cal'
    return x

def Dish_get_info() -> Dish:
    '''Promopt user for fields of Dish; create and return'''
    return Dish(
        input("Please enter the Dish's name: "),
        float(input("Please enter the Dish's price: ")),
        int(input("Please enter the Dish's calories: ")))

def Dish_change_price(d: Dish, f: float)->Dish:
    return (Dish(d.name,d.price*(1+(f*.01)), d.calories))

def Dish_prices(d: Dish)-> list:
    prices = []
    for x in d:
        prices.append(x.price)
    return prices

def Dish_calories(d: Dish)-> list:
    calories = []
    for x in d:
        calories.append(x.calories)
    return calories

#### MENUS

def Menu_enter() -> list:
    result = []
    add = input("Do you want to add a dish? (y/n) ")
    while add == 'y':
        result.append(Dish_get_info())
        add = input('Would you like to add a dish? (y/n): ')
    return result

def Menu_str(m: list) -> str:
    result = ''
    for x in m:
        result += Dish_str(x)+ "\n"
    result +='\n'
    return result

def Menu_change_price(d: list, f: float):
    for i in range(len(d)):
        d[i] = (Dish_change_price(d[i], f))

def Menu_averages(d: Dish) -> float:

    prices = Dish_prices(d)
    cost = 0
    for i in prices:
        cost += i
    return cost / len(prices)

def Menu_name(dish: list, title: str ) -> bool:
    for x in dish:
        if title in x.name:
            return True
    return False

def Menu_calories(d: Dish) -> float:
    calories = Dish_calories(d)
    cal = 0
    for i in calories:
        cal += i
    return cal / len(calories)


##### Restaurant

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50, [menu])

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n" +
        "{}: {}. {}: {}".format('Average price', str(Menu_averages(self.menu)), 'Average calories',
                                str(Menu_calories(self.menu))) + "\n"
        "Menu:     " + Menu_str(self.menu))

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")),
        Menu_enter())


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_change_prices(d:list, f: float):
    for x in d:
        Menu_change_price(x.menu,f)

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result

def Collection_search_by_cuisine(Collection: list):
    ''' Returns restaurants with inputed cuisine and avg. price '''
    cuisine = str(input('Enter the cuisine: '))

    result = []
    for x in Collection:
        if x.cuisine == cuisine:
            result.append(x)
    print(Collection_str(result))


def Collection_search_by_dish(Collection: list):
    dish = str(input('Enter enter the dish name: '))

    results = []
    for x in Collection:
        if Menu_name(x.menu, dish):
            results.append(x)
    print(Collection_str(results))

restaurants()