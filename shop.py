from article import Article


def main():
    article_list = []
    article_name = input('Artikelname > ')
    while article_name != 'Exit':
        if article_name == 'Inventory':
            handle_inventory(article_list)
            article_name = input('Artikelname > ')
            continue
        else:
            article = find_article(article_list, article_name)

            if article is None:
                article = Article(article_name, 0.0, 0)
                article_list.append(article)
                article.price = input_float('Preis       > ')
            else:
                print('Bestand     : ' + str(article.stock))

            amount = input_int('Menge       > ')
            article.stock = (article.stock + amount)
            article_name = input('Artikelname > ')

    return article_list


def handle_inventory(articlelist):
    """
    prints the inventory and the total value
    :param articlelist: the article list
    :return: None
    """
    total = 0
    for article in articlelist:
        total = total + article.article_value
        print(article.name + ' : ' + str(article.article_value))
    print('Gesamt : ' + str(total))


def input_int(prompt):
    """
    reads an integer input from the user
    :param prompt: the prompt to be shown
    :return: the integer number
    """
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('Please, enter a whole number!')
            continue
    return number


def input_float(prompt):
    """
    reads a decimal number input from the user
    :param prompt: the prompt to be shown
    :return: the decimal number
    """
    number = None
    while number is None:
        try:
            number = float(input(prompt))
        except ValueError:
            print('Please, enter a real number!')
            continue
    return number


def find_article(articlelist, name):
    """
    finds an article in the article list
    :param articlelist: the article list
    :param name: the article name to be found
    :return: article or None=not found
    """
    for article in articlelist:
        if article.name == name:
            return article
    return None


if __name__ == '__main__':
    print(main().__repr__())
