# Library Management System

## Problem Statement
Small libraries, educational institutions, or personal book collections often rely on manual paper logs or complex, heavyweight software to track inventory and lending operations. Manual tracking is prone to errors, data misplacement, and inefficient lookups, while full-scale database software can be over-engineered for simple management needs. A lightweight, terminal-based application is required to systematically organize book records and streamline cataloging, borrowing, and returning workflows.

## Scope of the Project
This project provides an in-memory, command-line interface (CLI) application developed in Python. 

* **In-Scope:**
  * Interactive CLI menu for navigating library operations[cite: 2].
  * Book collection management including adding, viewing, searching, and removing book records[cite: 1, 2].
  * Lending management to handle book issues and returns with dynamic status updates (`available` / `borrowed`)[cite: 1, 3].
  * Input validation for numeric inputs and valid book statuses[cite: 1].
  * Modular code design split across functional modules (`main.py`, `semi_file.py`, `book_issue.py`)[cite: 1, 2, 3].

* **Out-of-Scope:**
  * Persistent database storage (e.g., SQL/NoSQL databases or file storage like JSON/CSV).
  * Graphical User Interface (GUI) or Web Interface.
  * User authentication or detailed patron management (e.g., track member history/fines).

## Target Users
* **Library Administrators / Librarians:** To manage small-scale library inventories, add new entries, and remove decommissioned books.
* **Front-Desk Staff:** To quickly search for books, verify availability, and execute issue/return transactions.
* **Students and Hobbyists:** To study modular Python architecture, list-based data structures, and CLI flow design.

## High-Level Features
1. **Book Cataloging:**
   * **Add Books:** Register books with attributes including ID, title, author, initial status, and price[cite: 1].
   * **View Books:** Display all currently stored books in tabular output format[cite: 1, 2].
   * **Find Book:** Search and display details for a specific book using its unique ID[cite: 1, 2].
   * **Remove Book:** Delete a book record permanently from the collection using its ID[cite: 1, 2].

2. **Lending Operations:**
   * **Issue Book:** Transition a book status from `available` to `borrowed` upon validation[cite: 3].
   * **Return Book:** Transition a book status from `borrowed` to `available` upon return[cite: 3].

3. **User Experience & Safety:**
   * **CLI Interactive Navigation:** Choice-based main menu driving execution flow[cite: 2].
   * **Error Handling:** Guard clauses against invalid data types (e.g., non-numeric inputs for prices) or unrecognized input choices[cite: 1, 2].
