from random import randint
import random
import pyttsx3
import json

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Open json file
def quote_from_json(file, key):
    quotes = []
    with open(file) as f:
        data = json.load(f)
        for each in data:
            quotes.append(each[key])
    return quotes

# From the json file, get a random quote, and print/speech it
def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]  # get a quote from a list
    print(item)
    speakText(item)
    return item  # return the item

# Get de quote of the day every day at the same hour.
def quote_of_the_day():
    all_values = quote_from_json("quote.json", "quote")
    return get_random_item_in(all_values)