# library system to keep track of books 
#this is main file of the project
#********************************start of the code********************************

#importing the other files of the project

import semi_file
import book_issue

#data of the project

l=[["book_id","book_name","author_name","book_status","book_price"]]

#main loop of the project

while True:
    print("Welcome to the Library System")
    #giving the user the options to choose from
    print("1. Add a book")
    print("2. View all books")
    print("3. remove a book")
    print("4. Find a book")
    print("5. to issue a book")   
    print("6. to return a book")     
    print("7. Exit")
    
    #taking the user input for the choice
    
    choice = input("Enter your choice: ")
    
    #calling the functions
    
    if choice == '1':
        l=semi_file.add_book(l)
        
    elif choice == '2':
        semi_file.view_books(l)
        
    elif choice == '3':
        l=semi_file.remove_book(l)
    elif choice == '4':
        semi_file.find_book(l)
    elif choice == '5':
        l=semi_file.book_issue(l)
    elif choice == '6':
        l=semi_file.book_return(l)
    elif choice == '7':
        print("Exiting the Library System. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
        
##********************************end of the code********************************
#                                                                  -by Aman rawat