from kwManager import KwManager
from KwDB import Kw_Suggest_DB_Manipulate

# Usage:
# "python main.py" and input the keyword you want to know the suggestions.

def main():
    query = input('please input query: ')
    ks = KwManager(query=query)
    record = ks.create_record()
    print("record='{}'".format(record))

    # Kws = Kw_Suggest_DB_Manipulate()
    # Kws.CREATETABLE_KwSuggest('histry')
    # record="2021-03-03 11:00:00,gold,kabuka,kakaku,sakimono"
    # Kws.INSERT_KwSuggest(record)

if __name__ == "__main__":
    main()
