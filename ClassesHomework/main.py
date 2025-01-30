from classes import book

book1 = book()

book1.print_info()

book1.change_title("Harry Potter and the Sorcerer's Stone")
book1.change_author("JK Rowling")
book1.change_language("English")
book1.change_pages("223")

book1.print_info()

book1.time_to_complete()