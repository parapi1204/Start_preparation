import os
from time import sleep
import requests
import urllib.parse


class GoogleKwSuggester:
    """
    Get keyword suggestions for query on Google search Engine.
    """

    def __init__(self, test_mode=False, recurse_mode=False):
        self.base_url = "https://www.google.com/complete/search?"\
                        "client=firefox&q="
        self.test = test_mode
        self.recurse_mode = recurse_mode

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        characters = open('table_hiragana.txt', 'r')
        char_list = []
        for c in characters:
            c = c.rstrip()
            char_list.append(c)

        if test_mode:
            self.chrs = ['あ', 'g', '1']
        else:
            self.chrs = [str(i) for i in char_list]

    def get_suggest(self, query: str) -> list:
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        suggests = [ph for ph in buf[1]]
        print("query: [{0}]({1})".format(query, len(suggests)))
        for ph in suggests:
            print(" ", ph)
        sleep(1)
        return suggests

    def get_suggest_with_one_char(self, query: str) -> list:
        suggests = self.get_suggest(query)  # Suggestions for "query"
        suggests.extend(self.get_suggest(query + ' '))  # For "query "
        for ch in self.chrs:  # For "query ch"
            suggests.extend(self.get_suggest(query + ' ' + ch))

        if self.recurse_mode:
            suggests = self.get_uniq(suggests)
            addonelevel = []
            for ph in suggests:
                addonelevel.extend(self.get_suggest(ph + ' '))
            suggests.extend(addonelevel)

        return self.get_uniq(suggests)

    def get_uniq(self, arr: list) -> list:
        uniq_arr = []
        for x in arr:
            if x not in uniq_arr:
                uniq_arr.append(x)
        return uniq_arr
