import requests
import random
import tkinter as tk


quote_number = random.randint(1,1643)
def random_quote(quote_index):

    api_url = "https://type.fit/api/quotes"
    response = requests.get(api_url).json()

    quote_text = response[quote_index]['text']
    quote_author = response[quote_index]['author']
    return quote_text, quote_author



def print_quote():
    quote, author = random_quote(quote_number)
    return f"Today's quote: \n{quote} \nby author {author}"



#_________________________________________________________________________________________
#Creating display to print quote
def main():
    root = tk.Tk()
    root.title("QuoteMaster")
    root.configure(background="black")

    text = print_quote()
    label = tk.Label(root, text=text, font=("Arial", 16), fg= "blue", background="black")

    label.pack(pady=20)
    root.mainloop()
main()