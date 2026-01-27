######################################################################
#
#   Function name : BookStore
#   Description   : Prints the Book name,Book author,No of Bbooks
#   Author        : Shubham Shankarlal Kumawat
#   Date          : 27/01/2026
#
######################################################################

class BookStore:
    
    NoOfBooks = 0
    
    def __init__(self):
        self.Name = ""
        self.Author = ""

        print("Enter name of the book :")
        self.Name = input()

        print("Enter Author name :")
        self.Author = input()

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"Book:{self.Name} by {self.Author}. No of Books:{BookStore.NoOfBooks}")

Obj1 = BookStore()  
Obj1.Display()

obj2  = BookStore()
obj2.Display()
#######################################################################################################################
#
#   Input1 : C Book,Dennis Ritchie               Output : Book: C Book by Dennis Ritchie . No of Books: 1
#
#   Input2 : Python Basics,Guido van Rossum      Output : Book: Python Basics by Guido van Rossum . No of Books: 2
#
#######################################################################################################################