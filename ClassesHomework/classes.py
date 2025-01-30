class book():
    # class attribute
    material = "paper"

    # to create item of class book
    def __init__(self):
        self.title = input("Title of book: ")
        self.author = input("Author of book: ")
        self.language = input("Language of book: ")
        self.pages = input("Number of pages of book: ")


    # info funciton of class book
    def print_info(self):
        print(f"\n{self.title} was written by {self.author} in {self.language} and is {self.pages} pages long.\n")


    # changing values of class book
    def change_title(self, name):
        self.title = name

    def change_author(self, author):
        self.author = author

    def change_language(self, language):
        self.language = language

    def change_pages(self, pages):
        self.pages = pages

    
    # preform a calculation
    def time_to_complete(self):
        RawTime = input("How many minutes does it take to read one page of the book?: ")

        minutes = int(RawTime) * int(self.pages)

        if minutes < 60:
            print(f"It will take {int(minutes)} minutes to complete {self.title}.")
        else:
            hours = minutes / 60
            newMinutes = (hours % 1) * 60
            print(f"It will take {int(hours)} hours and {int(newMinutes)} minutes to complete {self.title}")