import requests
import random
import tkinter as tk

quote_number = random.randint(1, 10)


def random_quote(quote_index):
    api_url = "https://type.fit/api/quotes"
    response = requests.get(api_url).json()

    quote_text = response[quote_index]['text']
    quote_author = response[quote_index]['author']
    return quote_text, quote_author


def print_quote():
    quote, author = random_quote(quote_number)
    return f"\n{quote} \n         ---by author {author}"

