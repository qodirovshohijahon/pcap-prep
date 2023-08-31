"""
    Book Shelf
    Create a Book class that has two attributes:
        .title
        .author
        and two methods:

    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.
    and instantiate this class by creating 3 new books:

    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)
    The name of the new instances should be PP, H, and WP, respectively.

    For instance, if I instantiated the following book using this Book class:

    Harry Potter - J.K. Rowling (HP)
    I would get the following attributes and methods:

    Examples
        HP.title ➞ "Harry Potter"
        HP.author ➞ "J.K. Rowling"
        HP.get_title() ➞ "Title: Harry Potter"
        HP.get_author() ➞ "Author: J.K. Rowling"

"""
class Book:
	# Write your attributes and methods here
            def __init__(self, title, author) -> None:
                self.title = title
                self.author = author
            
            def get_title(self):
                return "Title: " + self.title

            def get_author(self):
                return "Author: " + self.author
            
            
WP = Book('War and Peace', 'Leo Tolstoy')
PP = Book('Pride and Prejudice','Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
HP = Book('Harry Potter', 'J.K. Rowling')

# print(HP.title) #➞ "Harry Potter"
# print(HP.author) #➞ "J.K. Rowling"
# print(HP.get_title()) #➞ "Title: Harry Potter"
# print(HP.get_author()) #➞ "Author: J.K. Rowling")
