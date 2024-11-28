import wikipedia

searched_term = input("Enter page title: ")
while searched_term != "":
    try:
        article_summary = wikipedia.summary(searched_term)
    except wikipedia.exceptions.PageError:
        print(f"Page id '{searched_term}' does not match any pages. Try another id!")
        searched_term = input("Enter article name: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    print(wikipedia.page(searched_term).title)
    print(article_summary)
    print(wikipedia.page(searched_term).url)
    searched_term = input("Enter article name: ")
print("Thank you.")