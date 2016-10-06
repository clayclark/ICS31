
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)


hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:', '$', rate)
print('Weekly salary:', '$', hours * rate)


name = input('Hello. What is your name? ')
print('Hello,', name)
print("It's nice to meet you.")
age = int(input('How old are you? '))
print('Next year you will be', age + 1, 'years old')
print('Good-bye!')


krone_per_euro = 7.46
krone_per_pound = 8.60
krone_per_dollar = 6.62

print('Please provide this information:')
name = input('Business name: ')
numOfEuros = int(input('Number of euros: '))
numOfPounds = int(input('Number of pounds: '))
numOfDollars = int(input('Number of dollars: '))

EuroToKrone = krone_per_euro * numOfEuros
PoundToKrone = krone_per_pound * numOfPounds
DollarToKrone = krone_per_dollar * numOfDollars

print('Copenhagen Chamber of Commerce')
print(numOfEuros, 'euros is', EuroToKrone, 'krone')
print(numOfPounds, 'pounds is', PoundToKrone, 'krone')
print(numOfDollars, 'dollars is', DollarToKrone, 'krone')

print('Total krone: ', EuroToKrone + PoundToKrone + DollarToKrone)


from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
new = Book('Return of Sherlock Holmes', 'Arthur Conan Doyle',
           1905, 26.00)
new_price = Book('Return of Sherlock Holmes', 'Arthur Conan Doyle',
           1905, 26.00 * 1.2)
booklist = [favorite, another, still_another]

print(still_another.title)
print(another.price)
print((favorite.price + another.price + still_another.price) / 3)
print(favorite.year < 1900)


Animal = namedtuple('Animal', 'name species age weight food')
elephant = Animal('Jumbo', 'elephant', 50, 1000, 'peanuts')
platypus = Animal('Perry', 'platypus', 7, 1.7, 'shrimp')

print(elephant.weight > platypus.weight)

print(booklist[0].price < booklist[1].price)
print(booklist[0].year > booklist[-1].year)


Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
# best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs",
               10.50) ]

print(RC[2].name)
print(RC[0].cuisine == RC[3].cuisine)
print(RC[-1].price)
RC.sort()
print(RC)
print(RC[-1].dish)
newList1 = [RC[0:2]]
newList2 = [RC[-2:]]
print(newList1, newList2)


import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 100, 300, fill='orange') 
my_canvas.create_line(100, 100, 300, 100, fill='orange')   
my_canvas.create_line(300, 100, 300, 300, fill='orange')
my_canvas.create_line(100, 300, 300, 300, fill='orange') # Square

my_canvas.create_line(200, 100, 300, 200, fill='blue')
my_canvas.create_line(300, 200, 200, 300, fill='blue')
my_canvas.create_line(200, 300, 100, 200, fill='blue')
my_canvas.create_line(100, 200, 200, 100, fill='blue') # Diamond

my_canvas.create_line(100, 100, 100, 300, fill='red') 
my_canvas.create_line(100, 100, 300, 100, fill='red')   
my_canvas.create_line(300, 100, 300, 300, fill='red')
my_canvas.create_line(100, 300, 300, 300, fill='red')
my_canvas.create_line(100, 100, 200, 0, fill='red')
my_canvas.create_line(200, 0, 300, 100, fill='red')
my_canvas.create_line(150, 300, 150, 200, fill='red')
my_canvas.create_line(150, 200, 250, 200, fill='red')
my_canvas.create_line(250, 200, 250, 300, fill='red')
my_canvas.create_line(110, 175, 110, 125, fill='red')
my_canvas.create_line(110, 125, 150, 125, fill='red')
my_canvas.create_line(150, 125, 150, 175, fill='red')
my_canvas.create_line(150, 175, 110, 175, fill='red') # House

my_canvas.create_oval(100, 400, 400, 250, fill='white')
my_canvas.create_oval(175, 400, 325, 250, fill='blue')
my_canvas.create_oval(225, 300, 275, 350, fill='black') #Eye

my_canvas.create_line(100, 100, 100, 300, fill='red')    
my_canvas.create_line(300, 100, 300, 300, fill='red')
my_canvas.create_line(100, 300, 300, 300, fill='red')
my_canvas.create_line(150, 300, 150, 200, fill='red')
my_canvas.create_line(150, 200, 250, 200, fill='red')
my_canvas.create_line(250, 200, 250, 300, fill='red')
my_canvas.create_line(110, 175, 110, 125, fill='red')
my_canvas.create_line(110, 125, 150, 125, fill='red')
my_canvas.create_line(150, 125, 150, 175, fill='red')
my_canvas.create_line(150, 175, 110, 175, fill='red')
my_canvas.create_line(225, 175, 275, 175, fill='red')
my_canvas.create_line(275, 175, 275, 125, fill='red')
my_canvas.create_line(275, 125, 225, 125, fill='red')
my_canvas.create_line(225, 125, 225, 175, fill='red')
my_canvas.create_line(250, 175, 250, 125, fill='red')
my_canvas.create_line(225, 150, 275, 150, fill='red')
my_canvas.create_line(110, 150, 150, 150, fill='red')
my_canvas.create_line(130, 125, 130, 175, fill='red')
my_canvas.create_oval(235, 250, 240, 245, fill='red')
my_canvas.create_line(200, 300, 200, 200, fill='red')
my_canvas.create_polygon(100, 100, 200, 0, 300, 100, fill='red') # Extra House

tkinter.mainloop()          # Combine all the elements and display the window