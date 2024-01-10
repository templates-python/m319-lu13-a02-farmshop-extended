import shop
from article import Article


def test_class():
    article = Article('Kuhfladen', 99.45, 7)
    content = article.__repr__()
    assert content == 'Article(name=\'Kuhfladen\', price=99.45, stock=7)'

def test_class_article_value():
    article = Article('Kuhfladen', 99.45, 7)
    content = article.article_value
    assert content == 696.15

def test_list(monkeypatch, capsys):
    inputs = iter(['Ei', 0.75, 30, 'Käse', '45.95', '7', 'Ei', '-4', 'Käse', -1, 'Exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    list = shop.main().__repr__()
    assert list == '[Article(name=\'Ei\', price=0.75, stock=26.0), Article(name=\'Käse\', price=45.95, stock=6.0)]'

def test_output(monkeypatch, capsys):
    inputs = iter(['Ei', '0.75', '30', 'Käse', '45.95', '7', 'Ei', '-4', 'Käse', '-1', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    shop.main()
    captured = capsys.readouterr()
    assert captured.out == 'Bestand     : 30.0\nBestand     : 7.0\n'

def test_output_inventory(monkeypatch, capsys):
    inputs = iter(['Ei', '0.75', '30', 'Käse', '45.95', '7', 'Ei', '-4', 'Käse', '-1', 'Inventory', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    shop.main()
    captured = capsys.readouterr()
    assert captured.out == ('Bestand     : 30.0\n'
                            'Bestand     : 7.0\n'
                            'Ei : 19.5\n'
                            'Käse : 275.70000000000005\n'
                            'Gesamt : 295.20000000000005\n'
                            )
