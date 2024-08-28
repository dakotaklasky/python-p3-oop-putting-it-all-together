#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self._title = None
        self._page_count = None

        self.title = title
        self.page_count = page_count

    
    def get_title(self):
        return self._title
    
    def set_title(self, new_title):
        if isinstance(new_title,str):
            self._title = new_title.title()
       
    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")
    
    title = property(get_title,set_title)
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!" )