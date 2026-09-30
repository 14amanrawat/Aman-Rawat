#this is sub file of the library management system
#this file contains the functions to issue and return books in the library
#********************************start of the code********************************

# function to issue a book from the library
def book_issue(l):
    book_id=input("Enter the id of the book you want to issue: ")
    for i in range(len(l)):
        if l[i][0]==book_id:
            if l[i][3]=="available":
                l[i][3]="borrowed"
                print("Book issued successfully.")
                return l
            else:
                print("Book is already borrowed.")
                return l
    print("Book not found.")
    return l

# function to return a book to the library

def book_return(l):
    book_id=input("Enter the id of the book you want to return: ")
    for i in range(len(l)):
        if l[i][0]==book_id:
            if l[i][3]=="borrowed":
                l[i][3]="available"
                print("Book returned successfully.")
                return l
            else:
                print("Book is not borrowed.")
                return l
    print("Book not found.")
    return l

#********************************end of the code********************************
#                                                               -by Aman rawat