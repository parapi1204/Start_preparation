import os
import datetime
import requests
import urllib.parse
from time import sleep


class KwManager:
    def __init__(
        self,
        query: str,
        test_mode=False,
        recurse_mode=False
    ):
        self.query = query
        self.base_url = "https://www.google.com/complete/search?"\
                        "client=firefox&q="
        self.test = test_mode
        self.recurse_mode = recurse_mode

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        characters = open('table_hiragana.txt', 'r', encoding="utf-8")
        char_list = []
        for c in characters:
            c = c.rstrip()
            char_list.append(c)

        if test_mode:
            self.chrs = ['あ', 'g', '1']
        else:
            self.chrs = [str(i) for i in char_list]

    def create_record(self) -> str:
        """
        Returns the VALUES for INSERT to MySQL table.
        """
        record = []

        dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record.append(dt_now)
        record.append(self.query)
        record.extend(self._retrieve_suggests())
        return ','.join(record)


    def _retrieve_suggests(self) -> list:
        """
        Returns three suggest-keywords except query part.
        For example, query="test" and suggest-keyword="test english",
        use only "english".
        """
        query = self.query + ' '
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        suggests = [ph for ph in buf[1]]
        suggests = self._get_uniq(suggests)
        suggests = self._remove_querypart(suggests)
        
        try:
            suggests.remove(self.query)
        except ValueError:
            pass

        return suggests[0:3]

    def _get_uniq(self, suggests: list) -> list:
        uniq_suggests = []
        for x in suggests:
            if x not in uniq_suggests:
                uniq_suggests.append(x)
        return uniq_suggests

    def _remove_querypart(self, suggests: list) -> list:
        removed_suggests = []
        for x in suggests:
            x = x.replace(self.query, '').replace(' ', '')
            removed_suggests.append(x)
        return removed_suggests

