from kwExplorer.googleKwSuggester import GoogleKwSuggester

if __name__ == "__main__":
    phrase = input('please input query: ')
    gs = GoogleKwSuggester(test_mode=True)
    # gs = GoogleKwSuggester()
    # gs = GoogleKwSuggester(recurse_mode='--recurse')
    suggestions = gs.get_suggest_with_one_char(phrase)
