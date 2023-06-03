# Overview

This python code was written in order to demonstraite the compatability between the python language, and the SQL database software.
This program has two main purposes depending on how many times you have used it before. For the first time, it creates and populates
the database with the required fields. It then allows for one to read and edit the data as they see fit.

[Software Demo Video](https://youtu.be/9Gtb2R8UIno)

# Relational Database

This is a rather simple relational database, the first table has peoples names and interests, while the other table has their hobbies.
This is linked together by an ID value that is the same accross both tables. The reason that this is done is so that the information 
is a little easier to read and understand.

The first table called person, has an ID, name, last name, and 1-2 interests per entry.
The second table called hobby, has an ID, and 1-2 hobbies per entry.

# Development Environment

To create this software, I used python in visual studio code, and then checked the database in
MYSQL workbench.

I used the python mysql library to allow for database connectivity.

# Useful Websites

- [https://www.freecodecamp.org/](https://www.freecodecamp.org/)
- [https://www.geeksforgeeks.org/](https://www.geeksforgeeks.org/)

# Future Work

- Allow for any table to be edited.
- More creative freedom.
- Give user the option to create more tables to the database.
