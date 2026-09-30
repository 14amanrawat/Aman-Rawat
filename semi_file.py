#this is first file of the library management system
#this file contains the functions to add, remove, find and view books in the library
#********************************start of the code********************************
#function to add a book to the library

def add_book(l):
    a=[]
    # taking no of books to be added from user
    try:
        n=int(input("Enter the number of books you want to add: "))
    except ValueError:
        print("Invalid input")
        return l
    
    # taking book details from user 
    
    for i in range(n):
        try:
            print("------------------add book---------------------")
            book_name=input("Enter the name of the book:")
            author_name=input("Enter the name of the author:")
            book_id=input("Enter the id of the book:")
            book_status=input("Enter the status of the book (available/borrowed):")
            if book_status not in ["available", "borrowed"]:
                print("Invalid status")
                return l
            book_price=float(input("Enter the price of the book:"))
            print("------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return l
        
        # adding the book to the list
        
        a=[book_id,book_name,author_name,book_status,book_price]
        l.append(a)
    return l

# function to remove a book from the library

def remove_book(l):
    book_id=input("Enter the id of the book you want to remove: ")
    for i in range(len(l)):
        if l[i][0]==book_id:
            del l[i]
            print("Book removed ")
            return l
    print("not found.")
    return l

# function to find a book in the library

def find_book(l):
    book_id=input("Enter the id of the book you want to find: ")
    for book in l:
        if book[0]==book_id:
            print(book)
            return
    print("not found.")


# function to view all books in the library

def view_books(l):
    print("---------------------books---------------------------")
    for book in l:  
        print(book)
    print("-----------------------------------------------------")    
#********************************end of the code********************************
#                                                               -by Aman rawat