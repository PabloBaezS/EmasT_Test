from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)

    def get_title(self):
        return self.title

    def display(self):
        print(self.title)

class Book(Item):
    author = models.CharField(max_length=100)

class Newspaper(Item):
    info = models.DateField()

    def display(self):
        print(self.info())

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    # Display all items in the library
    def display_items(self):
        for item in self.items:
            print(item.display())  # Polymorphic method call
