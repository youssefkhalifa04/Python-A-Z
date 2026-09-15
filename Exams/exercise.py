class Author : 
    __name : str 
    __age : int
    def __init__(self , name , age ):
        self.__name = name
        self.__age = age 
    def get_name (self):
        return self.__name
    def get_age(self):
        return self.__age
    



class Book:
    __title:str
    __author: Author
    __pages:int
    __category :str
    def __init__(self,title,author,pages,category):
        self.__title=title
        self.__author=author
        self.__pages=pages
        self.__category=category
    def __str__(self):
        return f"{self.__title},{self.__pages}"
    def get_author_name(self):
        return self.__author.get_name()

    def get_category(self):
        return self.__category




class Library:
    __name:str
    __books:list[Book]


    def __init__(self,name):
        self.__name=name
        self.__books=[]
    def add_book(self,b:Book):
        self.__books.append(b)
    
    def __get_index(name , l) : 
        c = 0 
        for i in l : 
            if i == name : 
                return c 
            c += 1

    def add_and_create_book (self , title , author , pages , category) :
        new_book = Book(title , author , pages , category)

        self.__books.append(new_book)

    def show_books(self):
        for i in self.__books:
            print(f"{i}\n")
    def get_top_author(self):
        authors = []
        writings = []

        for i  in self.__books : 
            if i.get_author_name() in authors :
                idx = __get_index(i.get_author_name() , authors)
                writings[idx] +=1 
            else : 
                authors.append(i.get_author_name())
                writings.append(1)
        max = writings[0]
        idx_max = 0
        idx = 0
        for i in writings : 
            if i > max : 
                max = i
                idx_max = idx
            idx += 1
        

        return authors[idx_max]






# every function starts with get_ always written without any parameters and returns a value
# every function starts with set_ always written with a parameter and returns nothing