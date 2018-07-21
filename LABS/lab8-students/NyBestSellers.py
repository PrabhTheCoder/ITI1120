def create_books_2Dlist(file_name):
    """(str) -> list of list of str
    Returns a 2D list containing books and their information from a file.
    The list will contain the information in the format:
    Publication date(YYYY-MM-DD), Title, Author, Publisher, Genre.
    Preconditions: each line in the file specified contains information about
    a book. In the format Title, Author, Publisher, Publication date(DD/MM/YY),
    Genre.
    """
    file = open(file_name).read().splitlines()
    books = []
    for book in file:
        book = book.split("\t")
        tmp = book[3]
        tmp = tmp.split("/")
        year = tmp[2]
        tmp[2] = tmp[0].zfill(2)
        tmp[0] = year
        tmp = "-".join(tmp)
        book.remove(book[3])
        book.insert(0, tmp)
        books.append(book)
    return books

def search_by_year(books, year1, year2):
    """(list of list of str, int, int)
    Prints a list of books in the list books published
    between year1 and year2.

    Precondition: books is a list created from create_books2Dlist
    """
    print("All titles between", year1, "and", year2)
    
    for book in range(len(books)):
        this_book = books[book]
        date = this_book[0]
        year = int(date.split('-')[0])
        title = this_book[1]
        author = this_book[2]
        if year1 <= year <= year2:
            print(title,", by", author,"(" + date + ")")
