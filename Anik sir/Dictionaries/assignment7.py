# Assignment 7:
# Problem Statement:
# You are given a list of books and their corresponding authors.
# Create a dictionary where the keys are the book titles and the values are their authors.
# Then, find and print the author of a specific book, entered by the user.
# If found show the author of the book searched by the user else show not available in the dictionary.
# Given data
books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5']
bDict={}
for i in range(len(books)):
    bDict.update({books[i]:authors[i]})
print(bDict) 
book_name=input