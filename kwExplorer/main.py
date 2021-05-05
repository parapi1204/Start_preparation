from googleKwSuggester import GoogleKwSuggester

# Usage:
# "python main.py" and input the keyword you want to know the suggestions.

if __name__ == "__main__":
    phrase = input('please input query: ')
    gs = GoogleKwSuggester(test_mode=True)
    # gs = GoogleKwSuggester()
    # gs = GoogleKwSuggester(recurse_mode='--recurse')
    suggestions = gs.get_suggest_with_one_char(phrase)
