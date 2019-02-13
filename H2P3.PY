title = int(input(" What is the title of the your book?" ))
author = int(input(" What is the name of the author of your book?" ))
year = int(input(" What year was your book published in?" ))
pages = int(input(" How many pages are in your book?" ))
age_of_book = (2019 - year)
print("This book is" + str(age_of_book) + "years old.")
if (age_of_book < 10):
    print("This book is younger thatn ten years old.")
else: (age_of_book > 10):
    print("This book is at least ten years old.")
if (pages < 100):
    print("This book is a short book.")
elif (pages == 100 && 300):
    print("This book is an average book.")
else: 
    print("This book is a long book.")